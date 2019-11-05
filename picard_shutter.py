# picard shutter interface
import os
from ctypes import *
from atexit import register, unregister

__x64_BASE_PATH = './picard_lib/x64/'
__x86_BASE_PATH = './picard_lib/Win32/'
__stddel_dll = 'PiUSB.dll'

__ver_info = (0,1,0)
__version__ = '.'.join(map(str, __ver_info))


def _get_dll(base_path, dll_type):
    cwd = os.getcwd()
    os.chdir(base_path)
    dll = windll.LoadLibrary(dll_type)
    os.chdir(cwd)
    return dll


_PICARD_DLL = _get_dll(__x64_BASE_PATH,__stddel_dll)


PI_SHUTTER_OPEN =1
PI_SHUTTER_CLOSED =0

class PicardShutter:

    piConnectShutter = _PICARD_DLL.piConnectShutter
    piConnectShutter.restype = c_void_p
    piConnectShutter.argtypes = [POINTER(c_int),c_int]

    piDisconnectShutter = _PICARD_DLL.piDisconnectShutter
    piDisconnectShutter.restype = None
    piDisconnectShutter.argtypes = [c_void_p]

    piGetShutterState =  _PICARD_DLL.piGetShutterState
    piGetShutterState.restype = c_int
    piGetShutterState.argtypes = [POINTER(c_int), c_void_p]

    piSetShutterState = _PICARD_DLL.piSetShutterState
    piSetShutterState.restype = c_int
    piSetShutterState.argtypes = [c_int, c_void_p]

    def __init__(self, serial_num, initial_state=None):
        self.sn = serial_num
        self._err_num = c_int()
        self._state = c_int()
        self._handle = self.piConnectShutter(byref(self._err_num), self.sn)
        state_success = self.piGetShutterState(byref(self._state), self._handle)
        register(self.disconnect_shutter)

    def set_shutter_state(self, shutter_state):
        self.piSetShutterState(shutter_state, self._handle)
    
    @property
    def shutter_state(self):
        state_success = self.piGetShutterState(byref(self._state), self._handle)
        return PI_SHUTTER_OPEN if self._state else PI_SHUTTER_CLOSED

    def open_shutter(self):
        self.piSetShutterState(PI_SHUTTER_OPEN, self._handle)

    def close_shutter(self):
        self.piSetShutterState(PI_SHUTTER_CLOSED, self._handle)

    def disconnect_shutter(self):
        self.piDisconnectShutter(self._handle)
        unregister(self.disconnect_shutter)
    