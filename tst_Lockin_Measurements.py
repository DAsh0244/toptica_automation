#Code to capture images using Lockin Camera
""""
Import all libraries required
"""
from __future__ import division,print_function
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os, sys
import ctypes as ct
import serial
import serial.tools.list_ports
import time as t
import scipy.io as sio


from dl_motor import *
from shg import *
from time import sleep

# Lockin Camera Nested Functions

from msvcrt import getch

try:
    prgPath=os.environ["PROGRAMFILES"]
    sys.path.insert(0,prgPath+r'\Heliotis\heliCam\Python\wrapper')
    
except BaseException  as err:
    print('Path Error'+str(err))

try:
    from libHeLIC import *
except ImportError as exc:
    print ('-'*30)
    print("Error: failed to import libHeLIC module ({})".format(exc))
    print("Please check if the path to Python wrapper correct.")
    print("(libHeLICTester.py Line 18-25)")
    print("For more details look at the documentation from the heliSDK in python folder.")
    print ('-'*30)
    print("Press a key to exit...")
    getch()
    sys.exit()


handleLockin =LibHeLIC() # Make it Global Variable

def Init_Lockin(num_frames,frequency,cycles):

    
        print("Initializing Lockin Camera")
        heSys= handleLockin
        res = heSys.Open(0,sys='c3cam_sl70')
        SensTqp = int(round((70e6/(8*frequency)) - 30)) #from Helicam C3 Manual Pg No - Update it
        SensNavM2 = int(cycles/2)
        settings = (
            ('AcqStop',1),
            ('CamMode',0),
            ('SensTqp',SensTqp),
            ('SensNavM2',SensNavM2),
            ('SensNFrames',num_frames),
            ('BSEnable',1),
            ('DdsGain',2),
            ('TrigFreeExtN',1),
            ('InvEncCnt',0),
            ('AcqStop',0)
          );
            # ('TrigExtSrcSel',0),
        for k,v in settings:
            try:
              setattr(heSys.map,k,v)#heSys.map.k=v
            except RuntimeError:
              error('Could not set map property %s to %s',k,v)
        return


def captureFrames_Lockin(num_frames, frequency):
   
    heSys = handleLockin
   
    def flushBuffer():
        
        try:
            setattr(heSys.map,"TrigFreeExtN",0)
        except RuntimeError:
            error('Could not set map property %s to %s',"TrigFreeExtN",0)    
        
        retVal = 0
        
        while retVal != -116:
            heSys.AllocCamData(1,LibHeLIC.CamDataFmt['DF_I16Q16'],0,0,0);
            retVal = heSys.Acquire()
            #print(retVal)
        print("flushed the buffer", retVal)    
        
        try:
            setattr(heSys.map,"TrigFreeExtN",1)
        except RuntimeError:
            error('Could not set map property %s to %s',"TrigFreeExtN",1)       
    
        return    
    
    flushBuffer()
    
    #Capture frames
    heSys.AllocCamData(1,LibHeLIC.CamDataFmt['DF_I16Q16'],0,0,0);
    retVal = heSys.Acquire()
    print("Acquired I and Q", retVal)
    cd=heSys.ProcessCamData(1,0,0)
    meta = heSys.CamDataMeta()
    img=heSys.GetCamData(1,0,ct.byref(meta))
    data=img.contents.data #Find out why you need to do this
    data=LibHeLIC.Ptr2Arr(data,(num_frames, 300, 300, 2),ct.c_ushort)    

    return data



def Disconnect_Lockin():
    
    hesys = handleLockin
    hesys.Close()
    print("disconnected lockin")
    return


# Thorlabs Shutter Nested Function
   
def INIT_ThorlabsShutter():
    availablePorts = getAvailablePorts()
    for portName in availablePorts:
        try:
            ser = serial.Serial(portName,timeout = 2)
            ser.write(b"0in")
            response = ser.readline().decode('utf-8')
            deviceSerialNumber = "10600114"
            ret = response.find(deviceSerialNumber)
            
            if ret == -1:
                 ser.close() 
            else:
                print("Thorlabs Shutter Initialized", portName)
                ser.write(b"0ho0")
                break
        except Exception as e:
            print("Cannot be opened", portName)
            print(e)
        
    return ser

def getAvailablePorts():
    ports = list(serial.tools.list_ports.comports())
    portList = []
    for port_no, description, address in ports:
        portList.append(port_no)
    
    return portList

def blockTheBeam(handle, block):
    
    if block == 1:
        handle.write(b"0fw")
        print("Object beam blocked")
        sleep(1.0)
    else:
        handle.write(b"0ho0")
        sleep(1.0)
    return


def Disconnect_ThorlabsShutter(handle):
    try:
        handle.close()
        print("Thorlabs shutter disconnected")
    except:
        print("can't close the port")
    
    return

if __name__ == "__main__":
    import numpy as np
        
    def nm2thz(nm):
        return (299792458/(nm*1e-9))*1e-12

    # Input Paramters
    demodulationFrequency = 10e3
    demodulationCycles = 20  
    numFrames = 10
    frames_lockin = np.ones([2,numFrames,300,300,2],np.uint16)
    start_freq = nm2thz(1119.0)
    # stop_wave = 1120.0
    steps = 5
    step_size_thz = -0.0625
    sweep = [start_freq+(step_size_thz*step) for step in range(steps)]
        

    #initialize motor
    # motor = DLMotor('COM4',home=True,enforce_limits=False)
    from shg import SHGpro
    from wavemeter import WavemeterDFC as Wavemeter
    wavemeter = Wavemeter('192.168.1.1')
    shg_pro = SHGpro('192.168.1.2','COM4')
    motor = shg_pro.motor
    # print(wavemeter._conn.recv(1024))
    from copy import deepcopy
    shg_pro.set_power_stabilization(False)
    thresholds = {
        1119:0.34,
        1119.25:0.34,
        1119.5:0.34,
        1120:0.34,
        }

    # Initialize the lockin camera and the Thorlabs Shutter
    Init_Lockin(numFrames,demodulationFrequency,demodulationCycles)
    serialporthandle = INIT_ThorlabsShutter()
    data = []
    
    # print('setting wavelength')
    # motor.set_wavelength(1120)
    # sleep(6.0)
    # err = wavemeter.measure_wavelength()*1e9
    # motor.wavelength_offset = 1120 - err
    
    # for i,wavelength in enumerate(np.linspace(1119,1120,5)):
    for i,freq in enumerate(sweep):
        shg_pro.set_power_stabilization(False)
        # motor.set_wavelength(wavelength)
        motor.set_frequency(freq)
        # shg.send((("(param-set! 'laser1:nlo:shg:lock:window:threshold {})\n").format(thresholds[wavelength])).encode('utf-8'))
        shg_pro.set_shg_relock_threshold(thresholds.get(freq,0.5))
        sleep(6.0)
        # meas_wavelength = wavemeter.measure_frequency()*1e9
        meas_freq = wavemeter.measure_frequency()*1e-12
        print(freq)
        print(meas_freq)
        print(meas_freq - freq)
        # shg.send(b"(param-set! 'laser1:power-stabilization:enabled #t )\n")
        shg_pro.set_power_stabilization(True)
        blockTheBeam(serialporthandle,1)
        print('shutter')
        sleep(6.0)
        frames = captureFrames_Lockin(numFrames, demodulationFrequency)
        frames_lockin[0,:,:,:,:] = deepcopy(frames)

        del frames
        blockTheBeam(serialporthandle,0)
        print('shutter')
        sleep(6.0)
        referenceFrames = captureFrames_Lockin(numFrames, demodulationFrequency)
        frames_lockin[1,:,:,:,:] = referenceFrames
        data.append((i,deepcopy(frames_lockin),meas_freq*2))
        del referenceFrames
    shg_pro.set_power_stabilization(False)
    data_dict = {'data_{}'.format(datum[0]+1):[datum[1],datum[2]] for datum in data}
    sio.savemat('point_source_frequency_sweep_09_26_2019_1452.mat',data_dict)

    wavemeter.close()
    shg_pro.close()
    # Disconnect LockIn camera and Shutter
    Disconnect_Lockin()
    # Disconnect_ThorlabsShutter(serialporthandle)
