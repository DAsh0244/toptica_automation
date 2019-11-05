"""wrapper for heliotis lock-in camera"""

from atexit import ( register as _register, unregister as _unregister )

import logging as _logging


_formatter = _logging.Formatter('%(asctime)s -  %(name)s - %(message)s')
logger = _logging.getLogger(__file__)
# logger = _logging.getLogger('A')
# logger.setLevel(logging.DEBUG)  # defaults to logging.WARNING
_ch = _logging.StreamHandler()
_ch.setLevel(_logging.DEBUG)
_ch.setFormatter(_formatter)
logger.addHandler(_ch)
logger.setLevel(_logging.DEBUG)


import ctypes as _ct
import sys
import os
import os.path as osp

try:
    pwd = os.getcwd()
    os.chdir(osp.join(os.environ["PROGRAMFILES"],'Heliotis','heliCam','Python','wrapper'))
    sys.path.insert(0,'')
    from libHeLIC import *
    sys.path.pop(0)
    os.chdir(pwd)
    del pwd
except ImportError as exc:
    print ('-'*30)
    print("Error: failed to import libHeLIC module ({})".format(exc))
    print("Please check if the path to Python wrapper correct.")
    print("(libHeLICTester.py Line 18-25)")
    print("For more details look at the documentation from the heliSDK in python folder.")
    print ('-'*30)
    print("Press a key to exit...")
    sys.exit()


class LockinCamera:

    good_keys = {
        # 'AcqStop',
        'CamMode',
        'SensTqp',
        'SensNavM2',
        'SensNFrames',
        'BSEnable',
        'DdsGain',
        'TrigFreeExtN',
        'InvEncCnt',
        'TrigExtSrcSel'
        }

    def __init__(self,name,lock_in_freq,cycles,num_frames,settings=None):
        self._handle  = LibHeLIC()
        self._name = name
        self._lock_in_freq = lock_in_freq
        self._cycles = cycles
        try:
            self._handle.Open(0,sys=self._name)
        except Exception as e:
            print(e)
            raise RuntimeError('Unable to open camera')
        _register(self.close) 
        self.settings = {
            'CamMode': 0,
            'SensNFrames': num_frames,
            'SensNavM2': int(cycles/2),
            'SensTqp': int(round((70e6/(8*self._lock_in_freq)) - 30)), #from Helicam C3 Manual Pg No - Update it
            'SensDeltaExp': 0,
            'BSEnable': 1,
            'DdsGain': 2,
            'TrigFreeExtN': 0,
            'InvEncCnt': 0,
        }
        if settings is not None:
            self.settings.update({k: settings[k] for k in self.good_keys})
        logger.debug('SensTqp %s', self.settings['SensTqp'])
        logger.debug('SensNavM2 %s', self.settings['SensNavM2'])
        self._update_settings()


    def _update_settings(self):
        self._set_property('AcqStop',1)
        for k,v in self.settings.items():
            self._set_property(k,v,False)
        self._set_property('AcqStop',0)

    def _set_property(self,prop,val, acq_stp=True):
        try:
            if acq_stp:
                setattr(self._handle.map, 'AcqStop',1)
                setattr(self._handle.map,prop,val)
                setattr(self._handle.map, 'AcqStop',0)
            else:
                setattr(self._handle.map,prop,val)
        except RuntimeError:
            logger.error('Could not set map property %s to %s',prop,val)    

    @property
    def cycles(self):
        return self._cycles
    
    @cycles.setter
    def cycles(self,val):
        self._cycles = val
        self.settings['SensNavM2'] = val
        self._set_property('SensNavM2',self.settings['SensNavM2'])

    @property
    def lock_in_freq(self):
        return self._lock_in_freq

    @lock_in_freq.setter
    def lock_in_freq(self,val):
        self._lock_in_freq = val
        self.settings['SensTqp']= int(round((70e6/(8*self._lock_in_freq)) - 30))
        self._set_property('SensTqp',self.settings['SensTqp'])

    @property
    def num_frames(self):
        return self.settings['SensNFrames']

    @num_frames.setter
    def num_frames(self,val):
        self.settings['SensNFrames'] = val
        self._set_property('SensNFrames',self.settings['SensNFrames'])

    @property
    def name(self):
        return self._name

    def flush_buffer(self):
        self._set_property('TrigFreeExtN',0)
        retVal = 0
        while retVal != -116:
            self._handle.AllocCamData(1,LibHeLIC.CamDataFmt['DF_I16Q16'],0,0,0)
            retVal = self._handle.Acquire()
            # logger.debug(retVal)
        logger.info("flushed the buffer: %s", retVal)  
        self._set_property('TrigFreeExtN',1)

    def capture_frames(self):
        self.flush_buffer()
        self._handle.AllocCamData(1,LibHeLIC.CamDataFmt['DF_I16Q16'],0,0,0)
        retVal = self._handle.Acquire()
        logger.info("Acquired I and Q: %s", retVal)
        # cd=self._handle.ProcessCamData(1,0,0)
        self._handle.ProcessCamData(1,0,0)
        meta = self._handle.CamDataMeta()
        img=self._handle.GetCamData(1,0,_ct.byref(meta))
        data=img.contents.data #Find out why you need to do this
        data=LibHeLIC.Ptr2Arr(data,(self.num_frames, 300, 300, 2),_ct.c_ushort)
        return data

    def close(self):
        logger.info('closing lockin')
        self._handle.Close()
        _unregister(self.close)

    # def __del__(self):
    #     try:
    #         self.close()
    #         _unregister(self.close)
    #     except Exception as e:
    #         print(e)
