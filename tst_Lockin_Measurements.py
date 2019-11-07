import os 
import os.path as osp
from time import sleep
from copy import deepcopy
import logging as _logging
from datetime import datetime
from multiprocessing import Event
from itertools import chain

import numpy as np
import scipy.io as sio

from shg import SHGpro
import lock_in_camera
# from thorlabs_shutter import ThorlabsShutter
from picard_shutter import PI_SHUTTER_OPEN, PI_SHUTTER_CLOSED, PicardShutter
from wavemeter import WavemeterDFC as Wavemeter
from laser_tuner import tune_laser_frequency, tune_laser_wavelength, nm2thz, thz2nm, c as C
from utils import time_execution



_formatter = _logging.Formatter('%(asctime)s -  %(name)s - %(message)s')
logger = _logging.getLogger(__file__)
# logger = _logging.getLogger('A')
# logger.setLevel(logging.DEBUG)  # defaults to logging.WARNING
_ch = _logging.StreamHandler()
_ch.setLevel(_logging.DEBUG)
_ch.setFormatter(_formatter)
logger.addHandler(_ch)
logger.setLevel(_logging.DEBUG)

ERROR = 'ERR'

 # Input Paramters
demodulationFrequency = 10e3
demodulationCycles = 80  
numFrames = 50
start_freq = nm2thz(1119.0)
STEPS = 4
# STEP_SIZE_THZ = -0.0625 # multiplied by 2 for master
STEP_SIZE_THZ = -0.037
S_BETWEEN_FRAMES = 1.0
FRAMES_CAPTURES = 1

thresholds = {
        -1:0.7
        # 1119:0.34,
        # 1119.25:0.34,
        # 1119.5:0.34,
        # 1120:0.34,
        }

# check these!!!
default_thresholds = {
    100:0.4,
    200:0.5,
    300:0.7,
    400:1.0,
    500:1.2,
    600:1.2,
    800:1.3,
}

default_currents = {
    100:2500.0,
    200:2950.0,
    300:3300.0,
    400:3800.0,
    500:4600.0,
    600:4000.0,
    800:4300.0,
}


# infrastructure vars
# THORLABS_SHUTTER_SN = 10600114
PICARD_SHUTTER_SN = 479
DFC_SERVER_IP = '192.168.1.1'
SHG_PRO_IP = '192.168.1.2'
SHG_PRO_MOTOR_ADDRESS = 'COM4'
LOCK_IN_CAM_NAME = 'c3cam_sl70'


SENSOR_PITCH = 39.6
# FILL_FACTOR = 0.5
FILL_FACTOR = 0.08
# MAG = 19.05
# 7.08
MAG = 24/1.2

SHG_POWER_mW = 800.0
TA_DEFAULT_CURRENT = default_currents[SHG_POWER_mW]
DEFAULT_THRESHOLD = default_thresholds[SHG_POWER_mW]
# TA_DEFAULT_CURRENT = 2900.0
# DEFAULT_THRESHOLD = 0.8

@time_execution('Acquisition', 'Starting Acquisition')
def acquire_data(exp_name):
    try: 
        TS = datetime.now().strftime('%m_%d_%Y_%H%M')
        EXP_NAME = exp_name
        OUTFILE_NAME = f'{EXP_NAME}_{TS}.mat'
        # raise RuntimeError()

        # data
        frames_lockin = np.ones([2,numFrames*FRAMES_CAPTURES,300,300,2],np.uint16)
        data = []
        sweep = [start_freq+(STEP_SIZE_THZ*step) for step in range(STEPS)]
        # sweep = [start_freq, start_freq+((STEPS-2)*STEP_SIZE_THZ)] # 267.76304378909737]
        # sweep = [267.9110437890974, 267.8370437890974, 267.9110437890974, 267.8000437890974] # 2mm, 1.35mm

        # n_entries = 1
        # ele = start_freq
        # lst = sweep[1:]
        # sweep = [sweep[0]]
        # sweep.extend(list(chain(*[lst[i:i+n_entries] + [ele] if len(lst[i:i+n_entries]) == n_entries else lst[i:i+n_entries] for i in range(0, len(lst), n_entries)]))[:-1])

        print(sweep)
        stop_event, stable_event = Event(), Event()

        # interfaces
        # shutter = ThorlabsShutter.from_serial_num(THORLABS_SHUTTER_SN)
        shutter = PicardShutter(PICARD_SHUTTER_SN)
        lockin = lock_in_camera.LockinCamera(LOCK_IN_CAM_NAME, demodulationFrequency, demodulationCycles, numFrames)
        wavemeter = Wavemeter(DFC_SERVER_IP)
        shg_pro = SHGpro(SHG_PRO_IP,SHG_PRO_MOTOR_ADDRESS)
        shg_pro.set_dl_current(200.0)
        shg_pro.set_dl_piezo(70.0)
        shg_pro.set_power_stabilization(False)
        shg_pro.set_power_stabilization_power(SHG_POWER_mW)
        
        # for i,wavelength in enumerate(np.linspace(1119,1120,5)):
        for i,freq in enumerate(sweep):
        # for i,freq in enumerate((0.0,140.0)):
            logger.info('starting sweep: %f' , freq)
            shg_pro.set_dl_current(200.0)
            shg_pro.set_dl_piezo(70.0)
            shg_pro.set_ta_current(TA_DEFAULT_CURRENT)
            shg_pro.set_power_stabilization(False)
            # shg_pro.motor.set_wavelength(wavelength)
            shg_pro.motor.set_frequency(freq)
            # measure err
            shg_pro.motor.wait_for_movement()
            curr_frequency = wavemeter.measure_frequency()*1e-12
            err = freq - curr_frequency 
            logger.debug('Error (THz): %f',err)
            # single pass grating correction:
            if abs(err) > 0.015:
                shg_pro.motor.frequency_offset = err
                shg_pro.motor.set_frequency(freq)
            shg_pro.set_shg_relock_threshold(thresholds.get(freq, DEFAULT_THRESHOLD))
            shg_pro.set_shg_temp_for_frequency(freq)
            # raise RuntimeError()
            logger.debug('starting PID')
            loop_handle = tune_laser_frequency(freq,shg_pro,wavemeter,stop_event,stable_event, log_file=f'pid_log_{i}.csv')
            while not stable_event.is_set():
                sleep(0.05)
            logger.debug('stabilized!')
            # meas_wavelength = wavemeter.measure_frequency()*1e9
            meas_freq = wavemeter.measure_frequency()*1e-12
            logger.info('target freq: %f', freq)
            logger.info('measured freq: %f', meas_freq)
            logger.info('Err: %f' , meas_freq - freq)
            shg_pro.set_power_stabilization(True)
            shutter.open_shutter()
            logger.info('shutter')
            # input('hit key to continue')
            sleep(1.0)

            # either this block
            frames = lockin.capture_frames()
            frames_lockin[0,:,:,:,:] = deepcopy(frames)

            # for j in range(FRAMES_CAPTURES):
            #     # print(slice(j*numFrames,((j+1)*numFrames)))
            #     frames = lockin.capture_frames()
            #     frames_lockin[0,j*numFrames:((j+1)*numFrames),:,:,:] = deepcopy(frames)
            #     sleep(S_BETWEEN_FRAMES)

            del frames
            shutter.close_shutter()
            logger.info('shutter')
            # input('hit key to continue')
            sleep(1.0)
            # ref_frames = numFrames*FRAMES_CAPTURES
            # lockin.num_frames = ref_frames
            referenceFrames = lockin.capture_frames()
            # print(np.shape(np.array(referenceFrames)))
            frames_lockin[1,:,:,:,:] = deepcopy(referenceFrames)
            # for j in range(FRAMES_CAPTURES):
            #     referenceFrames = lockin.capture_frames()
            #     frames_lockin[1,j*numFrames:((j+1)*numFrames),:,:,:] = deepcopy(referenceFrames)
            #     sleep(S_BETWEEN_FRAMES)
            data.append((i,deepcopy(frames_lockin),meas_freq*2))
            del referenceFrames
            # lockin.num_frames = numFrames
            logger.debug('stopping PID')
            stop_event.set()
            logger.debug('joining proc')
            loop_handle.join()
            loop_handle.close()
            stop_event.clear()
            stable_event.clear()
        shg_pro.set_power_stabilization(False)
        data_dict = {'data_{}'.format(datum[0]+1):[datum[1],datum[2]] for datum in data}
        data_dict['source_settings'] = {
            'num_shg_frequencies': len(sweep),
            'shg_power_mw': SHG_POWER_mW,
        }
        data_dict['camera_settings'] = {
            'magnification': MAG,
            'lock_in_settings' : lockin.settings,
            'sensor_pitch_um': SENSOR_PITCH,
            'px_pitch_VD_um': MAG*SENSOR_PITCH,
            'px_active_area_VD_um': MAG*SENSOR_PITCH*(FILL_FACTOR)**0.5,
        }
        data_dict['timestamp'] = TS

        sio.savemat(OUTFILE_NAME,data_dict)

        # reset for next
        shg_pro.set_power_stabilization(False)
        shg_pro.set_dl_current(200.0)
        shg_pro.set_dl_piezo(70.0)
        shg_pro.set_ta_current(2500.0)
        shg_pro.motor.set_frequency(start_freq)
        # # measure err
        # shg_pro.motor.wait_for_movement()
        # curr_frequency = wavemeter.measure_frequency()*1e-12
        # err = freq - curr_frequency 
        # logger.debug('Error (THz): %f',err)
        # # single pass grating correction:
        # if abs(err) > 0.015:
        #     shg_pro.motor.frequency_offset = err
        #     shg_pro.motor.set_frequency(start_freq)
        shg_pro.set_shg_relock_threshold(0.4)
        shg_pro.set_shg_temp_for_frequency(start_freq, block=False)
        shg_pro.set_power_stabilization_power(100.0)
        shutter.open_shutter()

        try:
            # shutter.close()
            shutter.disconnect_shutter()
        except Exception as e:
            logger.error(e)
        try:
            shg_pro.close()
        except Exception as e:
            logger.error(e)
        try:
            wavemeter.close()
        except Exception as e:
            logger.error(e)
        try:
            lockin.close()
        except Exception as e:
            logger.error(e)
        return osp.abspath(osp.join(os.curdir, OUTFILE_NAME))
    except Exception as e:
        logger.error(e)
        return ERROR

if __name__ == "__main__":
    import sys
    print(acquire_data(sys.argv[1]))
