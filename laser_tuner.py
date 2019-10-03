from shg import SHGpro
from wavemeter import WavemeterDFC
from PID import PID
from time import sleep, time
from multiprocessing import Event,Process
from utils import time_execution, logger

from socket import timeout, create_connection

PIEZO_MAX = 140.0
PIEZO_MIN = 0.0

wave_piezo_pid = PID(P=-120,I=-2400,D=-4)
freq_piezo_pid = PID(P=900,I=12000.0,D=30.0)
# wave_current_pid = PID(P=10,I=0,D=0)
# freq_current_pid = PID(P=10,I=0,D=0)
c = 299792458 # speed of light m/s
mode_hop_corrections = {
    # wavelength: {param1: val, param2:val}
    
}

def nm2thz(nm):
    return c/(nm*1e-9)/(1e12)


def thz2nm(thz):
    return c/(thz*1e12)/(1e-9)

def wavelength_pid_loop(wavelength:float, pid:PID,stop_event:Event, stable_event:Event, shg_addr:str, wavemeter_addr:str, 
                        piezo_max:float,piezo_min:float,log_file:str, sample_time:float,tol:float, stable_cnts_num:int):
    stable_event.clear()
    shg = SHGpro(shg_addr,None)
    wavemeter = WavemeterDFC(wavemeter_addr)
    piezo_offset = shg.get_dl_piezo()
    curr_wavelength = wavemeter.measure_wavelength()*1e9
    pid.clear()
    if pid.Ki != 0:
        pid.windup_guard = 3*(piezo_offset/abs(pid.Ki))
        pid.ITerm = piezo_offset/pid.Ki
    pid.SetPoint = wavelength
    pid.setSampleTime(0.5*sample_time)
    sleep(sample_time)
    # last_output = 70
    output = 0
    i=1
    stable_cnts = 0
    # print(pid.windup_guard, pid.ITerm, pid.ITerm * pid.Ki)
    with open(log_file,'w') as log:
        log.write('P={},I={},D={}\nTs={}\n'.format(pid.Kp,pid.Ki,pid.Kd,sample_time))
        log.write('Iteration,time(s),piezo_output,measured_wavelength(nm)\n')
        while not stop_event.is_set():
            curr_wavelength = wavemeter.measure_wavelength()*1e9
            # last_output = pid.output
            pid.update(curr_wavelength)   
            output = pid.output
            # adaptive time stepping
            # print(i,'piezo',output)
            print(pid.PTerm , (pid.Ki * pid.ITerm) ,(pid.Kd * pid.DTerm))
            shg.set_dl_piezo(max(min(piezo_max,output),piezo_min))
            sleep(sample_time)
            curr_wavelength = wavemeter.measure_wavelength()*1e9
            # print(wavelength, curr_wavelength)
            # print(abs(curr_wavelength - wavelength))
            i+=1
            log.write('{},{},{},{}\n'.format(i,i*sample_time,output,curr_wavelength))
            if abs(curr_wavelength - wavelength) < tol:
                stable_cnts += 1
            else:
                stable_cnts = 0
            if stable_cnts > stable_cnts_num:
                stable_event.set()
            else:
                stable_event.clear()

def frequency_pid_loop(frequency:float, pid:PID,stop_event:Event,stable_event:Event, shg_addr:str, wavemeter_addr:str, 
                       piezo_max:float,piezo_min:float,log_file:str, sample_time:float,tol:float, stable_cnts_num:int):
    stable_event.clear()
    shg = SHGpro(shg_addr,None)
    wavemeter = WavemeterDFC(wavemeter_addr)
    piezo_offset = shg.get_dl_piezo()
    curr_frequency = wavemeter.measure_frequency()*1e-12
    pid.clear()
    if pid.Ki != 0:
        pid.windup_guard = 3*(piezo_offset/abs(pid.Ki))
        pid.ITerm = piezo_offset/pid.Ki
    pid.SetPoint = frequency
    pid.setSampleTime(0.5*sample_time)
    sleep(sample_time)
    # last_output = 70
    output = 0
    i=1
    stable_cnts = 0
    # print(pid.windup_guard, pid.ITerm, pid.ITerm * pid.Ki)
    with open(log_file,'w') as log:
        log.write('P={},I={},D={}\nTs={}\n'.format(pid.Kp,pid.Ki,pid.Kd,sample_time))
        log.write('Iteration,time(s),piezo_output,measured_wavelength(nm)\n')
        while not stop_event.is_set():
            curr_frequency = wavemeter.measure_frequency()*1e-12
            # last_output = piezo_pid.output
            pid.update(curr_frequency)   
            output = pid.output
            # adaptive time stepping
            # print(i,'piezo',output)
            print(pid.PTerm , (pid.Ki * pid.ITerm) ,(pid.Kd * pid.DTerm))
            shg.set_dl_piezo(max(min(piezo_max,output),piezo_min))
            sleep(sample_time)
            curr_frequency = wavemeter.measure_frequency()*1e-12
            # print(frequency, curr_frequency)
            # print(abs(curr_frequency - frequency))
            i+=1
            log.write('{},{},{},{}\n'.format(i,i*sample_time,output,curr_frequency))
            if abs(curr_frequency - frequency) < tol:
                stable_cnts += 1
            else:
                stable_cnts = 0
            if stable_cnts > stable_cnts_num:
                stable_event.set()
            else:
                stable_event.clear()


# def tune_laser_wavelength(wavelength:float,sample_time:float=0.05,piezo_tol:float=0.0001,current_tol:float=0.00005,shg:SHGpro=shg,wavemeter:WavemeterDFC=wavemeter,piezo_pid:PID=wave_piezo_pid,dl_pid:PID=wave_current_pid):
def tune_laser_wavelength(wavelength:float,shg:SHGpro,wavemeter:WavemeterDFC,stop_event:Event,stable_event:Event,sample_time:float=0.05,
                          log_file:str='pid_log.csv',tol:float=0.000001,stable_cnts:int=10,piezo_pid:PID=wave_piezo_pid):
    # start shg crystal temperature
    shg.set_dl_current(200.0)
    shg.set_dl_piezo(70.0)
    keywords = {
        'wavelength': wavelength,
        'pid': piezo_pid,
        'stop_event': stop_event,
        'stable_event':stable_event,
        'shg_addr': shg._dlc_host,
        'wavemeter_addr': wavemeter._host,
        'piezo_max': PIEZO_MAX,
        'piezo_min': PIEZO_MIN,
        'log_file': log_file,
        'sample_time':sample_time,
        'tol':tol,
        'stable_cnts_num': stable_cnts,
        }
    pid_loop = Process(target=wavelength_pid_loop,kwargs=keywords)
    logger.debug('motor movement')
    # course adjust master motor
    shg.motor.set_wavelength(wavelength)
    # start temperature adjustment for SHG
    shg.set_shg_temp_for_wavelength(wavelength,block=True)
    pid_loop.start()
    return pid_loop

# def tune_laser_frequency(frequency:float,sample_time:float=0.05,piezo_tol:float=0.000001,current_tol:float=0.00005,shg:SHGpro=shg,wavemeter:WavemeterDFC=wavemeter,piezo_pid:PID=freq_piezo_pid,dl_pid:PID=freq_current_pid):
def tune_laser_frequency(frequency:float,shg:SHGpro,wavemeter:WavemeterDFC,stop_event:Event,stable_event:Event,sample_time:float=0.05, 
                         log_file:str='pid_log.csv',tol:float=0.000001,stable_cnts:int=10,piezo_pid:PID=freq_piezo_pid):
    # start shg crystal temperature
    shg.set_dl_current(200.0)
    shg.set_dl_piezo(70.0)
    keywords = {
        'frequency': frequency,
        'pid': piezo_pid,
        'stop_event': stop_event,
        'stable_event':stable_event,
        'shg_addr': shg._dlc_host,
        'wavemeter_addr': wavemeter._host,
        'piezo_max': PIEZO_MAX,
        'piezo_min': PIEZO_MIN,
        'log_file': log_file,
        'sample_time':sample_time,
        'tol':tol,
        'stable_cnts_num': stable_cnts,
        }
    pid_loop = Process(target=frequency_pid_loop,kwargs=keywords)
    logger.debug('motor movement')
    # course adjust master motor
    shg.motor.set_frequency(frequency)
    # measure err
    shg.motor.wait_for_movement()
    curr_frequency = wavemeter.measure_frequency()*1e-12
    err = frequency - curr_frequency 
    print(err)
    # single pass grating correction:
    if abs(err) > 0.015:
        shg.motor.frequency_offset = err
        shg.motor.set_frequency(frequency)
    # start temperature adjustment for SHG
    logger.debug('setting temp')
    shg.set_shg_temp_for_frequency(frequency,block=True)
    sleep(1.0)
    pid_loop.start()
    return pid_loop

if __name__ == "__main__":
    acq_time = 10
    stop_event, stable_event = Event(), Event()
    shg = SHGpro('192.168.1.2','COM4')
    wavemeter = WavemeterDFC('192.168.1.1')
    target_freq = nm2thz(1119)

    try:
        for freq in (target_freq, target_freq+0.125):
            print(freq)
            loop_handle = tune_laser_frequency(freq,shg,wavemeter,stop_event,stable_event)
            print('waiting to stabilize')
            while not stable_event.is_set():
                sleep(0.05)
            print('stabilized!')
            print('measuring freq for next {} seconds'.format(acq_time))
            stop_time = time() + acq_time
            while time() < stop_time:
                print(wavemeter.measure_frequency()*1e-12)
                sleep(1.0)
            stop_event.set()
            print('joining proc')
            loop_handle.join()
            loop_handle.close()
            # print(loop_handle.is_alive())
            # del loop_handle
            # print(wavemeter.measure_frequency())
            # print(shg.get_dl_piezo())
            # print(shg.motor._port.is_open)
            stop_event.clear()
            stable_event.clear()
    except KeyboardInterrupt:
        pass
