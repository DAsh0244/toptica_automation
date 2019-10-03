import os 
import os.path as osp
from time import sleep
from copy import deepcopy
from datetime import datetime
from multiprocessing import Event

import numpy as np
import scipy.io as sio

from shg import SHGpro
import lock_in_camera
from thorlabs_shutter import ThorlabsShutter
from wavemeter import WavemeterDFC as Wavemeter
from laser_tuner import tune_laser_frequency, tune_laser_wavelength, nm2thz, thz2nm, c as C
from utils import time_execution

ERROR = 'ERR'

 # Input Paramters
demodulationFrequency = 5e3
demodulationCycles = 80  
numFrames = 50
start_freq = nm2thz(1119.0)
STEPS = 5
STEP_SIZE_THZ = -0.0625 # multiplied by 2 for master

thresholds = {
        1119:0.34,
        1119.25:0.34,
        1119.5:0.34,
        1120:0.34,
        }

DEFAULT_THRESHOLD = 0.5

# infrastructure vars
THORLABS_SHUTTER_SN = 10600114
DFC_SERVER_IP = '192.168.1.1'
SHG_PRO_IP = '192.168.1.2'
SHG_PRO_MOTOR_ADDRESS = 'COM4'
LOCK_IN_CAM_NAME = 'c3cam_sl70'


SENSOR_PITCH = 39.6
FILL_FACTOR = 0.5
MAG = 19.05
SHG_POWER_mW = 200


@time_execution('Acquisition', 'Starting Acquisition')
def acquire_data(exp_name):
    TS = datetime.now().strftime('%m_%d_%Y_%H%M')
    EXP_NAME = exp_name
    OUTFILE_NAME = f'{EXP_NAME}_{TS}.mat'
    # raise RuntimeError()

    # data
    frames_lockin = np.ones([2,numFrames,300,300,2],np.uint16)
    data = []
    sweep = [start_freq+(STEP_SIZE_THZ*step) for step in range(STEPS)]
    stop_event, stable_event = Event(), Event()

    # interfaces
    shutter = ThorlabsShutter.from_serial_num(THORLABS_SHUTTER_SN)
    lockin = lock_in_camera.LockinCamera(LOCK_IN_CAM_NAME, demodulationFrequency, demodulationCycles, numFrames)
    wavemeter = Wavemeter(DFC_SERVER_IP)
    shg_pro = SHGpro(SHG_PRO_IP,SHG_PRO_MOTOR_ADDRESS)
    shg_pro.set_dl_current(200.0)
    shg_pro.set_dl_piezo(70.0)
    shg_pro.set_power_stabilization(False)
    
    # for i,wavelength in enumerate(np.linspace(1119,1120,5)):
    for i,freq in enumerate(sweep):
    # for i,freq in enumerate((0.0,140.0)):
        print('starting sweep:', freq)
        shg_pro.set_dl_current(200.0)
        shg_pro.set_dl_piezo(70.0)
        shg_pro.set_power_stabilization(False)
        # shg_pro.motor.set_wavelength(wavelength)
        shg_pro.motor.set_frequency(freq)
        shg_pro.set_shg_relock_threshold(thresholds.get(freq, DEFAULT_THRESHOLD))
        shg_pro.set_shg_temp_for_frequency(freq)
        # raise RuntimeError()
        print('starting PID')
        loop_handle = tune_laser_frequency(freq,shg_pro,wavemeter,stop_event,stable_event)
        while not stable_event.is_set():
            sleep(0.05)
        print('stabilized!')
        # meas_wavelength = wavemeter.measure_frequency()*1e9
        meas_freq = wavemeter.measure_frequency()*1e-12
        print('target freq:', freq)
        print('measured freq:', meas_freq)
        print('Err:', meas_freq - freq)
        shg_pro.set_power_stabilization(True)
        shutter.close_shutter()
        print('shutter')
        sleep(2.0)
        frames = lockin.capture_frames()
        frames_lockin[0,:,:,:,:] = deepcopy(frames)

        del frames
        shutter.open_shutter()
        print('shutter')
        sleep(2.0)
        referenceFrames = lockin.capture_frames()
        frames_lockin[1,:,:,:,:] = referenceFrames
        data.append((i,deepcopy(frames_lockin),meas_freq*2))
        del referenceFrames
        
        print('stopping PID')
        stop_event.set()
        print('joining proc')
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
    return osp.abspath(osp.join(os.curdir, OUTFILE_NAME))

if __name__ == "__main__":
    import sys
    print(acquire_data(sys.argv[1]))
