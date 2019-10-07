# toptica SHG control code:

from time import sleep
from dl_motor import DLMotor
from toptica.lasersdk.dlcpro.v2_0_3 import DLCpro, NetworkConnection, DeviceNotFoundError, DecopError, UserLevel
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


class fakeMotor:
    def close(*args):
        pass

class SHGpro:

    MASTER_TEMP_VS_WAVELENGTH= {
        'linear': [-1.12500000000000000E+00, 1.30593333333333000E+03],
        'quadratic':[2.63888888888885000E-02, -6.02361111111103000E+01, 3.44075222222217000E+04],
    }

    def __init__(self, dlc_address,motor_address, *args, **kwargs):
        self._dlc_host = dlc_address
        self.dlc = DLCpro(NetworkConnection(dlc_address)).__enter__()
        self.set_power_stabilization(False)
        if motor_address is not None:
            self.motor = DLMotor(motor_address,home=True)
        else:
            self.motor = fakeMotor()
        self.sleep_time = 1.0
        _register(self.close)

    def close(self):
        self.motor.close()
        self.dlc.__exit__()
        _unregister(self.close)
    
    def set_dl_piezo(self,voltage):
        self.dlc.laser1.dl.pc.voltage_set.set(voltage)

    def get_dl_piezo(self):
        return self.dlc.laser1.dl.pc.voltage_set.get()

    def set_dl_current(self,current):
        self.dlc.laser1.dl.cc.current_set.set(current)

    def get_dl_current(self):
        return self.dlc.laser1.dl.cc.current_set.get()

    def set_dl_temp(self,temp,block=False):
        self.dlc.laser1.dl.tc.temp_set.set(temp)
        if block:
            status = self.dl_temp_settled()
            while not status:
                sleep(self.sleep_time )
                status = self.dl_temp_settled()

    def get_dl_temp(self):
        return self.dlc.laser1.dl.tc.temp_set.get()

    def dl_temp_settled(self):
        return self.dlc.laser1.dl.tc.ready.get()

    def set_shg_temp(self,temp,block=False):
        self.dlc.laser1.nlo.shg.tc.temp_set.set(temp)
        if block:
            logger.debug('temp blocking')
            status = self.shg_temp_settled()
            while not status:
                sleep(self.sleep_time )
                status = self.shg_temp_settled()
            logger.debug('settled')

    def shg_temp_settled(self):
        return self.dlc.laser1.nlo.shg.tc.ready.get()

    def set_shg_lock(self,enable:bool=True):
        self.dlc.laser1.nlo.shg.lock.lock_enabled.set(enable)
    
    def set_shg_relock_threshold(self,threshold:float):
        self.dlc.laser1.nlo.shg.lock.window.threshold.set(threshold)
    
    def set_power_stabilization(self,enable:bool):
        self.dlc.laser1.power_stabilization.enabled.set(enable)
    
    def set_power_stabilization_power(self,power:float):
        self.dlc.laser1.power_stabilization.setpoint.set(power)

    def set_shg_temp_for_wavelength(self,wavelength,block=False,master:bool=True,mode='quadratic'):
        if not master:
            wavelength *= 2.0
        temp = self._horner_eval(self.MASTER_TEMP_VS_WAVELENGTH[mode],wavelength)
        self.set_shg_temp(temp,block=block)

    def set_shg_temp_for_frequency(self,frequency,block=False,master:bool=True,mode='quadratic'):
        wavelength = (299792458/(frequency*1e12))*1e9
        logger.debug('calculated wavelength %f', wavelength)
        self.set_shg_temp_for_wavelength(wavelength,block=block,master=master,mode=mode)

    def optimize_amplifier_power(self):
        pass
    def optimize_shg_power(self,advanced=False):
        pass
    def optimize_fiber_power(self):
        pass
    def optimize_power(self):
        pass

    @staticmethod
    def _horner_eval(coefficients,val):
        acc = 0
        for c in coefficients:
            acc = acc * val + c
        return acc

    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     # Don't pickle baz
    #     del state['motor']
    #     del state['close']
    #     del state['__del__']
        
    #     return state

    # def __del__(self):
    #     try:
    #         self.close()
    #     except Exception as e:
    #         print(e)
    #     _unregister(self.close)

