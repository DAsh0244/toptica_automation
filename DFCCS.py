# Generated from 'system.xml' on 2019-07-17 13:55:07.908014

from typing import Tuple

from toptica.lasersdk.client import UserLevel
from toptica.lasersdk.client import Client

from toptica.lasersdk.client import DecopBoolean
from toptica.lasersdk.client import DecopInteger
from toptica.lasersdk.client import DecopReal
from toptica.lasersdk.client import DecopString
from toptica.lasersdk.client import DecopBinary

from toptica.lasersdk.client import MutableDecopBoolean
from toptica.lasersdk.client import MutableDecopInteger
from toptica.lasersdk.client import MutableDecopReal
from toptica.lasersdk.client import MutableDecopString
from toptica.lasersdk.client import MutableDecopBinary

from toptica.lasersdk.client import Connection
from toptica.lasersdk.client import NetworkConnection
from toptica.lasersdk.client import SerialConnection

from toptica.lasersdk.client import DecopError
from toptica.lasersdk.client import DeviceNotFoundError


class DfcCore0011B894:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._system = System0734F5F0(client, name + ':system')
        self._sys_def = Sys_Def0734F9B0(client, name + ':sys_def')
        self._dev_mgr_sys = Dev_Mgr_Sys0734F110(client, name + ':dev_mgr_sys')

    @property
    def system(self) -> 'System0734F5F0':
        return self._system

    @property
    def sys_def(self) -> 'Sys_Def0734F9B0':
        return self._sys_def

    @property
    def dev_mgr_sys(self) -> 'Dev_Mgr_Sys0734F110':
        return self._dev_mgr_sys


class System0734F5F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._error_desc = DecopString(client, name + ':error_desc')
        self._state = DecopString(client, name + ':state')
        self._state_id = DecopInteger(client, name + ':state_id')

    @property
    def error_desc(self) -> 'DecopString':
        return self._error_desc

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def state_id(self) -> 'DecopInteger':
        return self._state_id


class Sys_Def0734F9B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._oscillator_current = DecopString(client, name + ':oscillator_current')
        self._repetition_rate = DecopString(client, name + ':repetition_rate')
        self._laser_on = DecopBoolean(client, name + ':laser_on')
        self._Oscillator = Oscillator0734F650(client, name + ':Oscillator')
        self._RepRateLock = Repratelock0734F7D0(client, name + ':RepRateLock')
        self._OpticalLock = Opticallock0734F350(client, name + ':OpticalLock')
        self._Safety = Safety0734F6B0(client, name + ':Safety')
        self._Emission = Emission0734Fbf0(client, name + ':Emission')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._DFGAmp = Dfgamp0734F890(client, name + ':DFGAmp')
        self._DistAmp = Distamp0734F710(client, name + ':DistAmp')
        self._EXT_1120 = Ext_11200734Fad0(client, name + ':EXT_1120')
        self._EXT_560 = Ext_5600734F950(client, name + ':EXT_560')
        self._Oscillator_set = MutableDecopBoolean(client, name + ':Oscillator_set')
        self._Oscillator_act = DecopBoolean(client, name + ':Oscillator_act')
        self._RepRateLock_set = MutableDecopBoolean(client, name + ':RepRateLock_set')
        self._RepRateLock_act = DecopBoolean(client, name + ':RepRateLock_act')
        self._DFGAmp_set = MutableDecopBoolean(client, name + ':DFGAmp_set')
        self._DFGAmp_act = DecopBoolean(client, name + ':DFGAmp_act')
        self._DistAmp_set = MutableDecopBoolean(client, name + ':DistAmp_set')
        self._DistAmp_act = DecopBoolean(client, name + ':DistAmp_act')
        self._EXT_1120_set = MutableDecopBoolean(client, name + ':EXT_1120_set')
        self._EXT_1120_act = DecopBoolean(client, name + ':EXT_1120_act')
        self._EXT_560_set = MutableDecopBoolean(client, name + ':EXT_560_set')
        self._EXT_560_act = DecopBoolean(client, name + ':EXT_560_act')

    @property
    def oscillator_current(self) -> 'DecopString':
        return self._oscillator_current

    @property
    def repetition_rate(self) -> 'DecopString':
        return self._repetition_rate

    @property
    def laser_on(self) -> 'DecopBoolean':
        return self._laser_on

    @property
    def Oscillator(self) -> 'Oscillator0734F650':
        return self._Oscillator

    @property
    def RepRateLock(self) -> 'Repratelock0734F7D0':
        return self._RepRateLock

    @property
    def OpticalLock(self) -> 'Opticallock0734F350':
        return self._OpticalLock

    @property
    def Safety(self) -> 'Safety0734F6B0':
        return self._Safety

    @property
    def Emission(self) -> 'Emission0734Fbf0':
        return self._Emission

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def DFGAmp(self) -> 'Dfgamp0734F890':
        return self._DFGAmp

    @property
    def DistAmp(self) -> 'Distamp0734F710':
        return self._DistAmp

    @property
    def EXT_1120(self) -> 'Ext_11200734Fad0':
        return self._EXT_1120

    @property
    def EXT_560(self) -> 'Ext_5600734F950':
        return self._EXT_560

    @property
    def Oscillator_set(self) -> 'MutableDecopBoolean':
        return self._Oscillator_set

    @property
    def Oscillator_act(self) -> 'DecopBoolean':
        return self._Oscillator_act

    @property
    def RepRateLock_set(self) -> 'MutableDecopBoolean':
        return self._RepRateLock_set

    @property
    def RepRateLock_act(self) -> 'DecopBoolean':
        return self._RepRateLock_act

    @property
    def DFGAmp_set(self) -> 'MutableDecopBoolean':
        return self._DFGAmp_set

    @property
    def DFGAmp_act(self) -> 'DecopBoolean':
        return self._DFGAmp_act

    @property
    def DistAmp_set(self) -> 'MutableDecopBoolean':
        return self._DistAmp_set

    @property
    def DistAmp_act(self) -> 'DecopBoolean':
        return self._DistAmp_act

    @property
    def EXT_1120_set(self) -> 'MutableDecopBoolean':
        return self._EXT_1120_set

    @property
    def EXT_1120_act(self) -> 'DecopBoolean':
        return self._EXT_1120_act

    @property
    def EXT_560_set(self) -> 'MutableDecopBoolean':
        return self._EXT_560_set

    @property
    def EXT_560_act(self) -> 'DecopBoolean':
        return self._EXT_560_act

    def system_on(self) -> None:
        self.__client.exec(self.__name + ':system_on', input_stream=None, output_type=None, return_type=None)

    def system_off(self) -> None:
        self.__client.exec(self.__name + ':system_off', input_stream=None, output_type=None, return_type=None)

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)

    def save_user_settings(self) -> None:
        self.__client.exec(self.__name + ':save_user_settings', input_stream=None, output_type=None, return_type=None)

    def delete_user_settings(self) -> None:
        self.__client.exec(self.__name + ':delete_user_settings', input_stream=None, output_type=None, return_type=None)


class Oscillator0734F650:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._repetition_rate = DecopString(client, name + ':repetition_rate')
        self._current_act = DecopString(client, name + ':current_act')
        self._run_current = MutableDecopReal(client, name + ':run_current')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._tec = Tec0734F830(client, name + ':tec')
        self._piezo_offset = MutableDecopReal(client, name + ':piezo_offset')
        self._piezo_voltage = DecopReal(client, name + ':piezo_voltage')
        self._frep_div_8_enabled = MutableDecopBoolean(client, name + ':frep_div_8_enabled')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def repetition_rate(self) -> 'DecopString':
        return self._repetition_rate

    @property
    def current_act(self) -> 'DecopString':
        return self._current_act

    @property
    def run_current(self) -> 'MutableDecopReal':
        return self._run_current

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def tec(self) -> 'Tec0734F830':
        return self._tec

    @property
    def piezo_offset(self) -> 'MutableDecopReal':
        return self._piezo_offset

    @property
    def piezo_voltage(self) -> 'DecopReal':
        return self._piezo_voltage

    @property
    def frep_div_8_enabled(self) -> 'MutableDecopBoolean':
        return self._frep_div_8_enabled

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Tec0734F830:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_set_timeout = MutableDecopReal(client, name + ':temp_set_timeout')
        self._pid_ki = MutableDecopReal(client, name + ':pid_ki')
        self._mode = MutableDecopBoolean(client, name + ':mode')
        self._pid_kd = MutableDecopReal(client, name + ':pid_kd')
        self._current_max = MutableDecopReal(client, name + ':current_max')
        self._error_desc = DecopString(client, name + ':error_desc')
        self._status_desc = DecopString(client, name + ':status_desc')
        self._temp_max = MutableDecopReal(client, name + ':temp_max')
        self._temp_max_diff = MutableDecopReal(client, name + ':temp_max_diff')
        self._status = DecopInteger(client, name + ':status')
        self._voltage_max = MutableDecopReal(client, name + ':voltage_max')
        self._error = DecopInteger(client, name + ':error')
        self._voltage_act = DecopReal(client, name + ':voltage_act')
        self._temp_min = MutableDecopReal(client, name + ':temp_min')
        self._current_act = DecopReal(client, name + ':current_act')
        self._temp_set = MutableDecopReal(client, name + ':temp_set')
        self._unit_id = DecopString(client, name + ':unit_id')
        self._pid_kp = MutableDecopReal(client, name + ':pid_kp')
        self._temp_act = DecopReal(client, name + ':temp_act')

    @property
    def temp_set_timeout(self) -> 'MutableDecopReal':
        return self._temp_set_timeout

    @property
    def pid_ki(self) -> 'MutableDecopReal':
        return self._pid_ki

    @property
    def mode(self) -> 'MutableDecopBoolean':
        return self._mode

    @property
    def pid_kd(self) -> 'MutableDecopReal':
        return self._pid_kd

    @property
    def current_max(self) -> 'MutableDecopReal':
        return self._current_max

    @property
    def error_desc(self) -> 'DecopString':
        return self._error_desc

    @property
    def status_desc(self) -> 'DecopString':
        return self._status_desc

    @property
    def temp_max(self) -> 'MutableDecopReal':
        return self._temp_max

    @property
    def temp_max_diff(self) -> 'MutableDecopReal':
        return self._temp_max_diff

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def voltage_max(self) -> 'MutableDecopReal':
        return self._voltage_max

    @property
    def error(self) -> 'DecopInteger':
        return self._error

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def temp_min(self) -> 'MutableDecopReal':
        return self._temp_min

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def unit_id(self) -> 'DecopString':
        return self._unit_id

    @property
    def pid_kp(self) -> 'MutableDecopReal':
        return self._pid_kp

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    def enable(self) -> None:
        self.__client.exec(self.__name + ':enable', input_stream=None, output_type=None, return_type=None)

    def disable(self) -> None:
        self.__client.exec(self.__name + ':disable', input_stream=None, output_type=None, return_type=None)

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Repratelock0734F7D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._frequency_difference = DecopString(client, name + ':frequency_difference')
        self._phase_error = DecopReal(client, name + ':phase_error')
        self._frequency_lock_gain = MutableDecopReal(client, name + ':frequency_lock_gain')
        self._piezo_pid_p = MutableDecopReal(client, name + ':piezo_pid_p')
        self._piezo_pid_i = MutableDecopReal(client, name + ':piezo_pid_i')
        self._piezo_pid_d = MutableDecopReal(client, name + ':piezo_pid_d')
        self._piezo_voltage = DecopReal(client, name + ':piezo_voltage')
        self._rf_ref_healthy = DecopBoolean(client, name + ':rf_ref_healthy')
        self._oscillator_frequency_stable = DecopBoolean(client, name + ':oscillator_frequency_stable')
        self._cycle_slip_detected = DecopBoolean(client, name + ':cycle_slip_detected')
        self._tec_i = MutableDecopReal(client, name + ':tec_i')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def frequency_difference(self) -> 'DecopString':
        return self._frequency_difference

    @property
    def phase_error(self) -> 'DecopReal':
        return self._phase_error

    @property
    def frequency_lock_gain(self) -> 'MutableDecopReal':
        return self._frequency_lock_gain

    @property
    def piezo_pid_p(self) -> 'MutableDecopReal':
        return self._piezo_pid_p

    @property
    def piezo_pid_i(self) -> 'MutableDecopReal':
        return self._piezo_pid_i

    @property
    def piezo_pid_d(self) -> 'MutableDecopReal':
        return self._piezo_pid_d

    @property
    def piezo_voltage(self) -> 'DecopReal':
        return self._piezo_voltage

    @property
    def rf_ref_healthy(self) -> 'DecopBoolean':
        return self._rf_ref_healthy

    @property
    def oscillator_frequency_stable(self) -> 'DecopBoolean':
        return self._oscillator_frequency_stable

    @property
    def cycle_slip_detected(self) -> 'DecopBoolean':
        return self._cycle_slip_detected

    @property
    def tec_i(self) -> 'MutableDecopReal':
        return self._tec_i

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    def cycle_slip_detector_reset(self) -> None:
        self.__client.exec(self.__name + ':cycle_slip_detector_reset', input_stream=None, output_type=None, return_type=None)

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Opticallock0734F350:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._piezo_pid_i = MutableDecopReal(client, name + ':piezo_pid_i')
        self._tec_i = MutableDecopReal(client, name + ':tec_i')
        self._piezo_voltage = DecopReal(client, name + ':piezo_voltage')
        self._piezo_offset = DecopReal(client, name + ':piezo_offset')
        self._piezo_step = MutableDecopReal(client, name + ':piezo_step')
        self._piezo_reset_rate = MutableDecopReal(client, name + ':piezo_reset_rate')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def piezo_pid_i(self) -> 'MutableDecopReal':
        return self._piezo_pid_i

    @property
    def tec_i(self) -> 'MutableDecopReal':
        return self._tec_i

    @property
    def piezo_voltage(self) -> 'DecopReal':
        return self._piezo_voltage

    @property
    def piezo_offset(self) -> 'DecopReal':
        return self._piezo_offset

    @property
    def piezo_step(self) -> 'MutableDecopReal':
        return self._piezo_step

    @property
    def piezo_reset_rate(self) -> 'MutableDecopReal':
        return self._piezo_reset_rate

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    def piezo_offset_increase(self) -> None:
        self.__client.exec(self.__name + ':piezo_offset_increase', input_stream=None, output_type=None, return_type=None)

    def piezo_offset_decrease(self) -> None:
        self.__client.exec(self.__name + ':piezo_offset_decrease', input_stream=None, output_type=None, return_type=None)

    def piezo_offset_reset(self) -> None:
        self.__client.exec(self.__name + ':piezo_offset_reset', input_stream=None, output_type=None, return_type=None)

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Safety0734F6B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._laser_class_4 = DecopBoolean(client, name + ':laser_class_4')
        self._laser_enable = DecopBoolean(client, name + ':laser_enable')
        self._interlock = DecopBoolean(client, name + ':interlock')
        self._state = DecopInteger(client, name + ':state')
        self._laser_lock = MutableDecopBoolean(client, name + ':laser_lock')
        self._remote_key = DecopBoolean(client, name + ':remote_key')
        self._unit_id = DecopString(client, name + ':unit_id')
        self._front_panel_key = DecopBoolean(client, name + ':front_panel_key')
        self._keylock = DecopBoolean(client, name + ':keylock')
        self._laser_disable = DecopBoolean(client, name + ':laser_disable')

    @property
    def laser_class_4(self) -> 'DecopBoolean':
        return self._laser_class_4

    @property
    def laser_enable(self) -> 'DecopBoolean':
        return self._laser_enable

    @property
    def interlock(self) -> 'DecopBoolean':
        return self._interlock

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def laser_lock(self) -> 'MutableDecopBoolean':
        return self._laser_lock

    @property
    def remote_key(self) -> 'DecopBoolean':
        return self._remote_key

    @property
    def unit_id(self) -> 'DecopString':
        return self._unit_id

    @property
    def front_panel_key(self) -> 'DecopBoolean':
        return self._front_panel_key

    @property
    def keylock(self) -> 'DecopBoolean':
        return self._keylock

    @property
    def laser_disable(self) -> 'DecopBoolean':
        return self._laser_disable


class Emission0734Fbf0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._off = DecopBoolean(client, name + ':off')
        self._unit_id = DecopString(client, name + ':unit_id')

    @property
    def off(self) -> 'DecopBoolean':
        return self._off

    @property
    def unit_id(self) -> 'DecopString':
        return self._unit_id


class Dfgamp0734F890:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._current_max = DecopReal(client, name + ':current_max')
        self._current_set = MutableDecopReal(client, name + ':current_set')
        self._power = DecopString(client, name + ':power')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def power(self) -> 'DecopString':
        return self._power

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Distamp0734F710:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._current_max = DecopReal(client, name + ':current_max')
        self._current_set = MutableDecopReal(client, name + ':current_set')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Ext_11200734Fad0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._current_max = DecopReal(client, name + ':current_max')
        self._current_set = MutableDecopReal(client, name + ':current_set')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Ext_5600734F950:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled_set = MutableDecopBoolean(client, name + ':enabled_set')
        self._enabled_act = DecopBoolean(client, name + ':enabled_act')
        self._state = DecopString(client, name + ':state')
        self._error = DecopString(client, name + ':error')
        self._current_max = DecopReal(client, name + ':current_max')
        self._current_set = MutableDecopReal(client, name + ':current_set')
        self._SHG_crystal_tec = Shg_Crystal_Tec0734F470(client, name + ':SHG_crystal_tec')
        self._SHG_power = DecopString(client, name + ':SHG_power')

    @property
    def enabled_set(self) -> 'MutableDecopBoolean':
        return self._enabled_set

    @property
    def enabled_act(self) -> 'DecopBoolean':
        return self._enabled_act

    @property
    def state(self) -> 'DecopString':
        return self._state

    @property
    def error(self) -> 'DecopString':
        return self._error

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def SHG_crystal_tec(self) -> 'Shg_Crystal_Tec0734F470':
        return self._SHG_crystal_tec

    @property
    def SHG_power(self) -> 'DecopString':
        return self._SHG_power

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Shg_Crystal_Tec0734F470:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_set_timeout = MutableDecopReal(client, name + ':temp_set_timeout')
        self._pid_ki = MutableDecopReal(client, name + ':pid_ki')
        self._mode = MutableDecopBoolean(client, name + ':mode')
        self._pid_kd = MutableDecopReal(client, name + ':pid_kd')
        self._current_max = MutableDecopReal(client, name + ':current_max')
        self._error_desc = DecopString(client, name + ':error_desc')
        self._status_desc = DecopString(client, name + ':status_desc')
        self._temp_max = MutableDecopReal(client, name + ':temp_max')
        self._temp_max_diff = MutableDecopReal(client, name + ':temp_max_diff')
        self._status = DecopInteger(client, name + ':status')
        self._voltage_max = MutableDecopReal(client, name + ':voltage_max')
        self._error = DecopInteger(client, name + ':error')
        self._voltage_act = DecopReal(client, name + ':voltage_act')
        self._temp_min = MutableDecopReal(client, name + ':temp_min')
        self._current_act = DecopReal(client, name + ':current_act')
        self._temp_set = MutableDecopReal(client, name + ':temp_set')
        self._unit_id = DecopString(client, name + ':unit_id')
        self._pid_kp = MutableDecopReal(client, name + ':pid_kp')
        self._temp_act = DecopReal(client, name + ':temp_act')

    @property
    def temp_set_timeout(self) -> 'MutableDecopReal':
        return self._temp_set_timeout

    @property
    def pid_ki(self) -> 'MutableDecopReal':
        return self._pid_ki

    @property
    def mode(self) -> 'MutableDecopBoolean':
        return self._mode

    @property
    def pid_kd(self) -> 'MutableDecopReal':
        return self._pid_kd

    @property
    def current_max(self) -> 'MutableDecopReal':
        return self._current_max

    @property
    def error_desc(self) -> 'DecopString':
        return self._error_desc

    @property
    def status_desc(self) -> 'DecopString':
        return self._status_desc

    @property
    def temp_max(self) -> 'MutableDecopReal':
        return self._temp_max

    @property
    def temp_max_diff(self) -> 'MutableDecopReal':
        return self._temp_max_diff

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def voltage_max(self) -> 'MutableDecopReal':
        return self._voltage_max

    @property
    def error(self) -> 'DecopInteger':
        return self._error

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def temp_min(self) -> 'MutableDecopReal':
        return self._temp_min

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def unit_id(self) -> 'DecopString':
        return self._unit_id

    @property
    def pid_kp(self) -> 'MutableDecopReal':
        return self._pid_kp

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    def enable(self) -> None:
        self.__client.exec(self.__name + ':enable', input_stream=None, output_type=None, return_type=None)

    def disable(self) -> None:
        self.__client.exec(self.__name + ':disable', input_stream=None, output_type=None, return_type=None)

    def reset(self) -> None:
        self.__client.exec(self.__name + ':reset', input_stream=None, output_type=None, return_type=None)


class Dev_Mgr_Sys0734F110:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._modules = Modules0734F1D0(client, name + ':modules')

    @property
    def modules(self) -> 'Modules0734F1D0':
        return self._modules


class Modules0734F1D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._sys = Sys0734F170(client, name + ':sys')

    @property
    def sys(self) -> 'Sys0734F170':
        return self._sys


class Sys0734F170:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._units = Units0734Fcb0(client, name + ':units')

    @property
    def units(self) -> 'Units0734Fcb0':
        return self._units


class Units0734Fcb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._laser_safety = Laser_Safety0734Fe90(client, name + ':laser_safety')
        self._emission = Emission07350370(client, name + ':emission')

    @property
    def laser_safety(self) -> 'Laser_Safety0734Fe90':
        return self._laser_safety

    @property
    def emission(self) -> 'Emission07350370':
        return self._emission


class Laser_Safety0734Fe90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._unit_id = DecopString(client, name + ':unit_id')
        self._interlock = DecopBoolean(client, name + ':interlock')
        self._keylock = DecopBoolean(client, name + ':keylock')
        self._laser_enable = DecopBoolean(client, name + ':laser_enable')
        self._front_panel_key = DecopBoolean(client, name + ':front_panel_key')
        self._remote_key = DecopBoolean(client, name + ':remote_key')
        self._laser_class_4 = DecopBoolean(client, name + ':laser_class_4')
        self._laser_disable = DecopBoolean(client, name + ':laser_disable')
        self._laser_lock = MutableDecopBoolean(client, name + ':laser_lock')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def unit_id(self) -> 'DecopString':
        return self._unit_id

    @property
    def interlock(self) -> 'DecopBoolean':
        return self._interlock

    @property
    def keylock(self) -> 'DecopBoolean':
        return self._keylock

    @property
    def laser_enable(self) -> 'DecopBoolean':
        return self._laser_enable

    @property
    def front_panel_key(self) -> 'DecopBoolean':
        return self._front_panel_key

    @property
    def remote_key(self) -> 'DecopBoolean':
        return self._remote_key

    @property
    def laser_class_4(self) -> 'DecopBoolean':
        return self._laser_class_4

    @property
    def laser_disable(self) -> 'DecopBoolean':
        return self._laser_disable

    @property
    def laser_lock(self) -> 'MutableDecopBoolean':
        return self._laser_lock


class Emission07350370:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._off = DecopBoolean(client, name + ':off')

    @property
    def off(self) -> 'DecopBoolean':
        return self._off


class Dlcpro000Daf74:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._DLC = Dlc00130490(client, name + ':DLC')

    @property
    def DLC(self) -> 'Dlc00130490':
        return self._DLC


class Dlc00130490:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._laser1 = Laser100130670(client, name + ':laser1')
        self._laser2 = Laser207407Ac0(client, name + ':laser2')

    @property
    def laser1(self) -> 'Laser100130670':
        return self._laser1

    @property
    def laser2(self) -> 'Laser207407Ac0':
        return self._laser2


class Laser100130670:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = DecopString(client, name + ':type')
        self._product_name = DecopString(client, name + ':product-name')
        self._emission = DecopBoolean(client, name + ':emission')
        self._health = DecopInteger(client, name + ':health')
        self._health_txt = DecopString(client, name + ':health-txt')
        self._dl = Dl000Df8F0(client, name + ':dl')
        self._ctl = Ctl00142560(client, name + ':ctl')
        self._amp = Amp001431C0(client, name + ':amp')
        self._dpss = Dpss073791C0(client, name + ':dpss')
        self._scan = Scan073790A0(client, name + ':scan')
        self._wide_scan = WideScan06E794C0(client, name + ':wide-scan')
        self._scope = Scope06E78800(client, name + ':scope')
        self._recorder = Recorder06E789E0(client, name + ':recorder')
        self._nlo = Nlo06E79220(client, name + ':nlo')
        self._uv = Uv071Eceb8(client, name + ':uv')
        self._pd_ext = PdExt074072E0(client, name + ':pd-ext')
        self._power_stabilization = PowerStabilization07407040(client, name + ':power-stabilization')
        self._config = Config074079A0(client, name + ':config')

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def product_name(self) -> 'DecopString':
        return self._product_name

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def health(self) -> 'DecopInteger':
        return self._health

    @property
    def health_txt(self) -> 'DecopString':
        return self._health_txt

    @property
    def dl(self) -> 'Dl000Df8F0':
        return self._dl

    @property
    def ctl(self) -> 'Ctl00142560':
        return self._ctl

    @property
    def amp(self) -> 'Amp001431C0':
        return self._amp

    @property
    def dpss(self) -> 'Dpss073791C0':
        return self._dpss

    @property
    def scan(self) -> 'Scan073790A0':
        return self._scan

    @property
    def wide_scan(self) -> 'WideScan06E794C0':
        return self._wide_scan

    @property
    def scope(self) -> 'Scope06E78800':
        return self._scope

    @property
    def recorder(self) -> 'Recorder06E789E0':
        return self._recorder

    @property
    def nlo(self) -> 'Nlo06E79220':
        return self._nlo

    @property
    def uv(self) -> 'Uv071Eceb8':
        return self._uv

    @property
    def pd_ext(self) -> 'PdExt074072E0':
        return self._pd_ext

    @property
    def power_stabilization(self) -> 'PowerStabilization07407040':
        return self._power_stabilization

    @property
    def config(self) -> 'Config074079A0':
        return self._config

    def save(self) -> None:
        self.__client.exec(self.__name + ':save', input_stream=None, output_type=None, return_type=None)

    def load(self) -> None:
        self.__client.exec(self.__name + ':load', input_stream=None, output_type=None, return_type=None)

    def load_head(self) -> None:
        self.__client.exec(self.__name + ':load-head', input_stream=None, output_type=None, return_type=None)


class Dl000Df8F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._legacy = DecopBoolean(client, name + ':legacy')
        self._type_ = DecopString(client, name + ':type')
        self._version = DecopString(client, name + ':version')
        self._model = DecopString(client, name + ':model')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._fru_serial_number = DecopString(client, name + ':fru-serial-number')
        self._ontime = DecopInteger(client, name + ':ontime')
        self._ontime_txt = DecopString(client, name + ':ontime-txt')
        self._cc = Cc06Fe4270(client, name + ':cc')
        self._tc = Tc06Fe3910(client, name + ':tc')
        self._pc = Pc06Fe3D30(client, name + ':pc')
        self._lock = Lock06Fe3A90(client, name + ':lock')
        self._pressure_compensation = PressureCompensation00142B60(client, name + ':pressure-compensation')
        self._pd = Pd001430A0(client, name + ':pd')
        self._factory_settings = FactorySettings00142980(client, name + ':factory-settings')

    @property
    def legacy(self) -> 'DecopBoolean':
        return self._legacy

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def version(self) -> 'DecopString':
        return self._version

    @property
    def model(self) -> 'DecopString':
        return self._model

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def fru_serial_number(self) -> 'DecopString':
        return self._fru_serial_number

    @property
    def ontime(self) -> 'DecopInteger':
        return self._ontime

    @property
    def ontime_txt(self) -> 'DecopString':
        return self._ontime_txt

    @property
    def cc(self) -> 'Cc06Fe4270':
        return self._cc

    @property
    def tc(self) -> 'Tc06Fe3910':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fe3D30':
        return self._pc

    @property
    def lock(self) -> 'Lock06Fe3A90':
        return self._lock

    @property
    def pressure_compensation(self) -> 'PressureCompensation00142B60':
        return self._pressure_compensation

    @property
    def pd(self) -> 'Pd001430A0':
        return self._pd

    @property
    def factory_settings(self) -> 'FactorySettings00142980':
        return self._factory_settings


class Cc06Fe4270:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._variant = DecopString(client, name + ':variant')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._emission = DecopBoolean(client, name + ':emission')
        self._current_set = MutableDecopReal(client, name + ':current-set')
        self._current_offset = MutableDecopReal(client, name + ':current-offset')
        self._current_set_dithering = MutableDecopBoolean(client, name + ':current-set-dithering')
        self._external_input = ExternalInput06Fe3790(client, name + ':external-input')
        self._output_filter = OutputFilter06Fe4210(client, name + ':output-filter')
        self._current_act = DecopReal(client, name + ':current-act')
        self._positive_polarity = DecopBoolean(client, name + ':positive-polarity')
        self._current_clip = MutableDecopReal(client, name + ':current-clip')
        self._current_clip_limit = DecopReal(client, name + ':current-clip-limit')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._pd = DecopReal(client, name + ':pd')
        self._aux = DecopReal(client, name + ':aux')
        self._snubber = DecopBoolean(client, name + ':snubber')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def variant(self) -> 'DecopString':
        return self._variant

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def current_offset(self) -> 'MutableDecopReal':
        return self._current_offset

    @property
    def current_set_dithering(self) -> 'MutableDecopBoolean':
        return self._current_set_dithering

    @property
    def external_input(self) -> 'ExternalInput06Fe3790':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter06Fe4210':
        return self._output_filter

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def positive_polarity(self) -> 'DecopBoolean':
        return self._positive_polarity

    @property
    def current_clip(self) -> 'MutableDecopReal':
        return self._current_clip

    @property
    def current_clip_limit(self) -> 'DecopReal':
        return self._current_clip_limit

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def pd(self) -> 'DecopReal':
        return self._pd

    @property
    def aux(self) -> 'DecopReal':
        return self._aux

    @property
    def snubber(self) -> 'DecopBoolean':
        return self._snubber

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput06Fe3790:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter06Fe4210:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Tc06Fe3910:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fe41B0(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fe39D0(client, name + ':t-loop')
        self._limits = Limits06Fe3C10(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fe41B0':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fe39D0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fe3C10':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fe41B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop06Fe39D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits06Fe3C10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc06Fe3D30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput06Fe3970(client, name + ':external-input')
        self._output_filter = OutputFilter06Fe3Fd0(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput06Fe3970':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter06Fe3Fd0':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput06Fe3970:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter06Fe3Fd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Lock06Fe3A90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = MutableDecopInteger(client, name + ':type')
        self._lock_without_lockpoint = MutableDecopBoolean(client, name + ':lock-without-lockpoint')
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._spectrum_input_channel = MutableDecopInteger(client, name + ':spectrum-input-channel')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock06Fe3Cd0(client, name + ':relock')
        self._reset = Reset06Fe3C70(client, name + ':reset')
        self._window = Window06Fe3F10(client, name + ':window')
        self._pid1 = Pid106Fe4150(client, name + ':pid1')
        self._pid2 = Pid206Fe44B0(client, name + ':pid2')
        self._lockin = Lockin00142Ec0(client, name + ':lockin')
        self._lockpoint = Lockpoint00142B00(client, name + ':lockpoint')
        self._candidate_filter = CandidateFilter00142C80(client, name + ':candidate-filter')
        self._candidates = DecopBinary(client, name + ':candidates')
        self._locking_delay = MutableDecopInteger(client, name + ':locking-delay')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def type_(self) -> 'MutableDecopInteger':
        return self._type_

    @property
    def lock_without_lockpoint(self) -> 'MutableDecopBoolean':
        return self._lock_without_lockpoint

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def spectrum_input_channel(self) -> 'MutableDecopInteger':
        return self._spectrum_input_channel

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock06Fe3Cd0':
        return self._relock

    @property
    def reset(self) -> 'Reset06Fe3C70':
        return self._reset

    @property
    def window(self) -> 'Window06Fe3F10':
        return self._window

    @property
    def pid1(self) -> 'Pid106Fe4150':
        return self._pid1

    @property
    def pid2(self) -> 'Pid206Fe44B0':
        return self._pid2

    @property
    def lockin(self) -> 'Lockin00142Ec0':
        return self._lockin

    @property
    def lockpoint(self) -> 'Lockpoint00142B00':
        return self._lockpoint

    @property
    def candidate_filter(self) -> 'CandidateFilter00142C80':
        return self._candidate_filter

    @property
    def candidates(self) -> 'DecopBinary':
        return self._candidates

    @property
    def locking_delay(self) -> 'MutableDecopInteger':
        return self._locking_delay

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace

    def show_candidates(self) -> None:
        self.__client.exec(self.__name + ':show-candidates', input_stream=None, output_type=None, return_type=None)

    def find_candidates(self) -> None:
        self.__client.exec(self.__name + ':find-candidates', input_stream=None, output_type=None, return_type=None)

    def select_lockpoint(self) -> None:
        self.__client.exec(self.__name + ':select-lockpoint', input_stream=None, output_type=None, return_type=None)

    def close(self) -> None:
        self.__client.exec(self.__name + ':close', input_stream=None, output_type=None, return_type=None)

    def open(self) -> None:
        self.__client.exec(self.__name + ':open', input_stream=None, output_type=None, return_type=None)


class Relock06Fe3Cd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Reset06Fe3C70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Window06Fe3F10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._level_high = MutableDecopReal(client, name + ':level-high')
        self._level_low = MutableDecopReal(client, name + ':level-low')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def level_high(self) -> 'MutableDecopReal':
        return self._level_high

    @property
    def level_low(self) -> 'MutableDecopReal':
        return self._level_low

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis


class Pid106Fe4150:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain06Fe4510(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._slope = MutableDecopBoolean(client, name + ':slope')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._outputlimit = Outputlimit06Fe4390(client, name + ':outputlimit')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._lock_state = DecopBoolean(client, name + ':lock-state')
        self._hold_state = DecopBoolean(client, name + ':hold-state')
        self._regulating_state = DecopBoolean(client, name + ':regulating-state')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain06Fe4510':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def slope(self) -> 'MutableDecopBoolean':
        return self._slope

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def outputlimit(self) -> 'Outputlimit06Fe4390':
        return self._outputlimit

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def lock_state(self) -> 'DecopBoolean':
        return self._lock_state

    @property
    def hold_state(self) -> 'DecopBoolean':
        return self._hold_state

    @property
    def regulating_state(self) -> 'DecopBoolean':
        return self._regulating_state


class Gain06Fe4510:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')
        self._fc_ip = DecopReal(client, name + ':fc-ip')
        self._fc_pd = DecopReal(client, name + ':fc-pd')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled

    @property
    def fc_ip(self) -> 'DecopReal':
        return self._fc_ip

    @property
    def fc_pd(self) -> 'DecopReal':
        return self._fc_pd


class Outputlimit06Fe4390:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._max = MutableDecopReal(client, name + ':max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def max(self) -> 'MutableDecopReal':
        return self._max


class Pid206Fe44B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain06Fe43F0(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._slope = MutableDecopBoolean(client, name + ':slope')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._outputlimit = Outputlimit00142Aa0(client, name + ':outputlimit')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._lock_state = DecopBoolean(client, name + ':lock-state')
        self._hold_state = DecopBoolean(client, name + ':hold-state')
        self._regulating_state = DecopBoolean(client, name + ':regulating-state')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain06Fe43F0':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def slope(self) -> 'MutableDecopBoolean':
        return self._slope

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def outputlimit(self) -> 'Outputlimit00142Aa0':
        return self._outputlimit

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def lock_state(self) -> 'DecopBoolean':
        return self._lock_state

    @property
    def hold_state(self) -> 'DecopBoolean':
        return self._hold_state

    @property
    def regulating_state(self) -> 'DecopBoolean':
        return self._regulating_state


class Gain06Fe43F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')
        self._fc_ip = DecopReal(client, name + ':fc-ip')
        self._fc_pd = DecopReal(client, name + ':fc-pd')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled

    @property
    def fc_ip(self) -> 'DecopReal':
        return self._fc_ip

    @property
    def fc_pd(self) -> 'DecopReal':
        return self._fc_pd


class Outputlimit00142Aa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._max = MutableDecopReal(client, name + ':max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def max(self) -> 'MutableDecopReal':
        return self._max


class Lockin00142Ec0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._modulation_enabled = MutableDecopBoolean(client, name + ':modulation-enabled')
        self._modulation_output_channel = MutableDecopInteger(client, name + ':modulation-output-channel')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')
        self._lock_level = MutableDecopReal(client, name + ':lock-level')
        self._auto_lir = AutoLir00142Da0(client, name + ':auto-lir')

    @property
    def modulation_enabled(self) -> 'MutableDecopBoolean':
        return self._modulation_enabled

    @property
    def modulation_output_channel(self) -> 'MutableDecopInteger':
        return self._modulation_output_channel

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    @property
    def lock_level(self) -> 'MutableDecopReal':
        return self._lock_level

    @property
    def auto_lir(self) -> 'AutoLir00142Da0':
        return self._auto_lir


class AutoLir00142Da0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._progress = DecopInteger(client, name + ':progress')

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    def auto_lir(self) -> None:
        self.__client.exec(self.__name + ':auto-lir', input_stream=None, output_type=None, return_type=None)


class Lockpoint00142B00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = DecopString(client, name + ':type')

    @property
    def type_(self) -> 'DecopString':
        return self._type_


class CandidateFilter00142C80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._top = MutableDecopBoolean(client, name + ':top')
        self._bottom = MutableDecopBoolean(client, name + ':bottom')
        self._positive_edge = MutableDecopBoolean(client, name + ':positive-edge')
        self._negative_edge = MutableDecopBoolean(client, name + ':negative-edge')
        self._edge_level = MutableDecopReal(client, name + ':edge-level')
        self._peak_noise_tolerance = MutableDecopReal(client, name + ':peak-noise-tolerance')
        self._edge_min_distance = MutableDecopInteger(client, name + ':edge-min-distance')

    @property
    def top(self) -> 'MutableDecopBoolean':
        return self._top

    @property
    def bottom(self) -> 'MutableDecopBoolean':
        return self._bottom

    @property
    def positive_edge(self) -> 'MutableDecopBoolean':
        return self._positive_edge

    @property
    def negative_edge(self) -> 'MutableDecopBoolean':
        return self._negative_edge

    @property
    def edge_level(self) -> 'MutableDecopReal':
        return self._edge_level

    @property
    def peak_noise_tolerance(self) -> 'MutableDecopReal':
        return self._peak_noise_tolerance

    @property
    def edge_min_distance(self) -> 'MutableDecopInteger':
        return self._edge_min_distance


class PressureCompensation00142B60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._air_pressure = DecopReal(client, name + ':air-pressure')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._compensation_voltage = DecopReal(client, name + ':compensation-voltage')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def air_pressure(self) -> 'DecopReal':
        return self._air_pressure

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def compensation_voltage(self) -> 'DecopReal':
        return self._compensation_voltage


class Pd001430A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class FactorySettings00142980:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._threshold_current = DecopReal(client, name + ':threshold-current')
        self._power = DecopReal(client, name + ':power')
        self._cc = Cc00143040(client, name + ':cc')
        self._tc = Tc001429E0(client, name + ':tc')
        self._pc = Pc00142620(client, name + ':pc')
        self._pd = Pd00142E60(client, name + ':pd')

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def threshold_current(self) -> 'DecopReal':
        return self._threshold_current

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cc(self) -> 'Cc00143040':
        return self._cc

    @property
    def tc(self) -> 'Tc001429E0':
        return self._tc

    @property
    def pc(self) -> 'Pc00142620':
        return self._pc

    @property
    def pd(self) -> 'Pd00142E60':
        return self._pd

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Cc00143040:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_clip = DecopReal(client, name + ':current-clip')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._positive_polarity = DecopBoolean(client, name + ':positive-polarity')
        self._snubber = DecopBoolean(client, name + ':snubber')

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_clip(self) -> 'DecopReal':
        return self._current_clip

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def positive_polarity(self) -> 'DecopBoolean':
        return self._positive_polarity

    @property
    def snubber(self) -> 'DecopBoolean':
        return self._snubber


class Tc001429E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')
        self._ntc_parallel_resistance = DecopReal(client, name + ':ntc-parallel-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance

    @property
    def ntc_parallel_resistance(self) -> 'DecopReal':
        return self._ntc_parallel_resistance


class Pc00142620:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._slew_rate = DecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = DecopBoolean(client, name + ':slew-rate-enabled')
        self._pressure_compensation_factor = DecopReal(client, name + ':pressure-compensation-factor')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def slew_rate(self) -> 'DecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'DecopBoolean':
        return self._slew_rate_enabled

    @property
    def pressure_compensation_factor(self) -> 'DecopReal':
        return self._pressure_compensation_factor


class Pd00142E60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Ctl00142560:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._fpga_fw_ver = DecopInteger(client, name + ':fpga-fw-ver')
        self._wavelength_set = MutableDecopReal(client, name + ':wavelength-set')
        self._wavelength_act = DecopReal(client, name + ':wavelength-act')
        self._wavelength_min = DecopReal(client, name + ':wavelength-min')
        self._wavelength_max = DecopReal(client, name + ':wavelength-max')
        self._tuning_current_min = DecopReal(client, name + ':tuning-current-min')
        self._tuning_power_min = DecopReal(client, name + ':tuning-power-min')
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._head_temperature = DecopReal(client, name + ':head-temperature')
        self._optimization = Optimization001426E0(client, name + ':optimization')
        self._remote_control = RemoteControl00142Bc0(client, name + ':remote-control')
        self._mode_control = ModeControl00142740(client, name + ':mode-control')
        self._motor = Motor001427A0(client, name + ':motor')
        self._power = Power001432E0(client, name + ':power')
        self._factory_settings = FactorySettings00143160(client, name + ':factory-settings')

    @property
    def fpga_fw_ver(self) -> 'DecopInteger':
        return self._fpga_fw_ver

    @property
    def wavelength_set(self) -> 'MutableDecopReal':
        return self._wavelength_set

    @property
    def wavelength_act(self) -> 'DecopReal':
        return self._wavelength_act

    @property
    def wavelength_min(self) -> 'DecopReal':
        return self._wavelength_min

    @property
    def wavelength_max(self) -> 'DecopReal':
        return self._wavelength_max

    @property
    def tuning_current_min(self) -> 'DecopReal':
        return self._tuning_current_min

    @property
    def tuning_power_min(self) -> 'DecopReal':
        return self._tuning_power_min

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def head_temperature(self) -> 'DecopReal':
        return self._head_temperature

    @property
    def optimization(self) -> 'Optimization001426E0':
        return self._optimization

    @property
    def remote_control(self) -> 'RemoteControl00142Bc0':
        return self._remote_control

    @property
    def mode_control(self) -> 'ModeControl00142740':
        return self._mode_control

    @property
    def motor(self) -> 'Motor001427A0':
        return self._motor

    @property
    def power(self) -> 'Power001432E0':
        return self._power

    @property
    def factory_settings(self) -> 'FactorySettings00143160':
        return self._factory_settings


class Optimization001426E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._progress = DecopInteger(client, name + ':progress')

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    def smile(self) -> None:
        self.__client.exec(self.__name + ':smile', input_stream=None, output_type=None, return_type=None)

    def flow(self) -> None:
        self.__client.exec(self.__name + ':flow', input_stream=None, output_type=None, return_type=None)

    def abort(self) -> None:
        self.__client.exec(self.__name + ':abort', input_stream=None, output_type=None, return_type=None)


class RemoteControl00142Bc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class ModeControl00142740:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._loop_enabled = MutableDecopBoolean(client, name + ':loop-enabled')

    @property
    def loop_enabled(self) -> 'MutableDecopBoolean':
        return self._loop_enabled


class Motor001427A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._position_accuracy_fullstep = DecopInteger(client, name + ':position-accuracy-fullstep')
        self._position_hysteresis_fullstep = DecopInteger(client, name + ':position-hysteresis-fullstep')
        self._position_accuracy_microstep = DecopInteger(client, name + ':position-accuracy-microstep')
        self._position_hysteresis_microstep = DecopInteger(client, name + ':position-hysteresis-microstep')
        self._microsteps = MutableDecopBoolean(client, name + ':microsteps')
        self._power_save_disabled = DecopBoolean(client, name + ':power-save-disabled')

    @property
    def position_accuracy_fullstep(self) -> 'DecopInteger':
        return self._position_accuracy_fullstep

    @property
    def position_hysteresis_fullstep(self) -> 'DecopInteger':
        return self._position_hysteresis_fullstep

    @property
    def position_accuracy_microstep(self) -> 'DecopInteger':
        return self._position_accuracy_microstep

    @property
    def position_hysteresis_microstep(self) -> 'DecopInteger':
        return self._position_hysteresis_microstep

    @property
    def microsteps(self) -> 'MutableDecopBoolean':
        return self._microsteps

    @property
    def power_save_disabled(self) -> 'DecopBoolean':
        return self._power_save_disabled


class Power001432E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_act = DecopReal(client, name + ':power-act')

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act


class FactorySettings00143160:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength_min = DecopReal(client, name + ':wavelength-min')
        self._wavelength_max = DecopReal(client, name + ':wavelength-max')
        self._tuning_current_min = DecopReal(client, name + ':tuning-current-min')
        self._tuning_power_min = DecopReal(client, name + ':tuning-power-min')

    @property
    def wavelength_min(self) -> 'DecopReal':
        return self._wavelength_min

    @property
    def wavelength_max(self) -> 'DecopReal':
        return self._wavelength_max

    @property
    def tuning_current_min(self) -> 'DecopReal':
        return self._tuning_current_min

    @property
    def tuning_power_min(self) -> 'DecopReal':
        return self._tuning_power_min

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Amp001431C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._legacy = DecopBoolean(client, name + ':legacy')
        self._type_ = DecopString(client, name + ':type')
        self._version = DecopString(client, name + ':version')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._fru_serial_number = DecopString(client, name + ':fru-serial-number')
        self._ontime = DecopInteger(client, name + ':ontime')
        self._ontime_txt = DecopString(client, name + ':ontime-txt')
        self._cc = Cc00143400(client, name + ':cc')
        self._tc = Tc07378860(client, name + ':tc')
        self._pd = Pd073788C0(client, name + ':pd')
        self._seed_limits = SeedLimits07378F20(client, name + ':seed-limits')
        self._output_limits = OutputLimits07378E60(client, name + ':output-limits')
        self._seedonly_check = SeedonlyCheck073789E0(client, name + ':seedonly-check')
        self._factory_settings = FactorySettings07378D40(client, name + ':factory-settings')

    @property
    def legacy(self) -> 'DecopBoolean':
        return self._legacy

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def version(self) -> 'DecopString':
        return self._version

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def fru_serial_number(self) -> 'DecopString':
        return self._fru_serial_number

    @property
    def ontime(self) -> 'DecopInteger':
        return self._ontime

    @property
    def ontime_txt(self) -> 'DecopString':
        return self._ontime_txt

    @property
    def cc(self) -> 'Cc00143400':
        return self._cc

    @property
    def tc(self) -> 'Tc07378860':
        return self._tc

    @property
    def pd(self) -> 'Pd073788C0':
        return self._pd

    @property
    def seed_limits(self) -> 'SeedLimits07378F20':
        return self._seed_limits

    @property
    def output_limits(self) -> 'OutputLimits07378E60':
        return self._output_limits

    @property
    def seedonly_check(self) -> 'SeedonlyCheck073789E0':
        return self._seedonly_check

    @property
    def factory_settings(self) -> 'FactorySettings07378D40':
        return self._factory_settings


class Cc00143400:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._variant = DecopString(client, name + ':variant')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._emission = DecopBoolean(client, name + ':emission')
        self._current_set = MutableDecopReal(client, name + ':current-set')
        self._current_offset = MutableDecopReal(client, name + ':current-offset')
        self._output_filter = OutputFilter00143460(client, name + ':output-filter')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_clip = MutableDecopReal(client, name + ':current-clip')
        self._current_clip_limit = DecopReal(client, name + ':current-clip-limit')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._voltage_out = DecopReal(client, name + ':voltage-out')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._aux = DecopReal(client, name + ':aux')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def variant(self) -> 'DecopString':
        return self._variant

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def current_offset(self) -> 'MutableDecopReal':
        return self._current_offset

    @property
    def output_filter(self) -> 'OutputFilter00143460':
        return self._output_filter

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_clip(self) -> 'MutableDecopReal':
        return self._current_clip

    @property
    def current_clip_limit(self) -> 'DecopReal':
        return self._current_clip_limit

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def voltage_out(self) -> 'DecopReal':
        return self._voltage_out

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def aux(self) -> 'DecopReal':
        return self._aux

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class OutputFilter00143460:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Tc07378860:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput07378C80(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop07378Ce0(client, name + ':t-loop')
        self._limits = Limits07378B60(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput07378C80':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop07378Ce0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits07378B60':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput07378C80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop07378Ce0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits07378B60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pd073788C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._seed = Seed07378A40(client, name + ':seed')
        self._amp = Amp07378980(client, name + ':amp')

    @property
    def seed(self) -> 'Seed07378A40':
        return self._seed

    @property
    def amp(self) -> 'Amp07378980':
        return self._amp


class Seed07378A40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp07378980:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class SeedLimits07378F20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class OutputLimits07378E60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class SeedonlyCheck073789E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._warning_delay = DecopReal(client, name + ':warning-delay')
        self._shutdown_delay = DecopReal(client, name + ':shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def warning_delay(self) -> 'DecopReal':
        return self._warning_delay

    @property
    def shutdown_delay(self) -> 'DecopReal':
        return self._shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class FactorySettings07378D40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._power = DecopReal(client, name + ':power')
        self._cc = Cc07378Da0(client, name + ':cc')
        self._tc = Tc07378F80(client, name + ':tc')
        self._pd = Pd07378Fe0(client, name + ':pd')
        self._seed_limits = SeedLimits073785C0(client, name + ':seed-limits')
        self._output_limits = OutputLimits07378800(client, name + ':output-limits')
        self._seedonly_check = SeedonlyCheck073786E0(client, name + ':seedonly-check')

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cc(self) -> 'Cc07378Da0':
        return self._cc

    @property
    def tc(self) -> 'Tc07378F80':
        return self._tc

    @property
    def pd(self) -> 'Pd07378Fe0':
        return self._pd

    @property
    def seed_limits(self) -> 'SeedLimits073785C0':
        return self._seed_limits

    @property
    def output_limits(self) -> 'OutputLimits07378800':
        return self._output_limits

    @property
    def seedonly_check(self) -> 'SeedonlyCheck073786E0':
        return self._seedonly_check

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Cc07378Da0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_clip = DecopReal(client, name + ':current-clip')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_clip(self) -> 'DecopReal':
        return self._current_clip

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip


class Tc07378F80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')
        self._ntc_parallel_resistance = DecopReal(client, name + ':ntc-parallel-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance

    @property
    def ntc_parallel_resistance(self) -> 'DecopReal':
        return self._ntc_parallel_resistance


class Pd07378Fe0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._seed = Seed07378500(client, name + ':seed')
        self._amp = Amp07378740(client, name + ':amp')

    @property
    def seed(self) -> 'Seed07378500':
        return self._seed

    @property
    def amp(self) -> 'Amp07378740':
        return self._amp


class Seed07378500:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp07378740:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class SeedLimits073785C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay


class OutputLimits07378800:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay


class SeedonlyCheck073786E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._warning_delay = DecopReal(client, name + ':warning-delay')
        self._shutdown_delay = DecopReal(client, name + ':shutdown-delay')

    @property
    def warning_delay(self) -> 'DecopReal':
        return self._warning_delay

    @property
    def shutdown_delay(self) -> 'DecopReal':
        return self._shutdown_delay


class Dpss073791C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._tc_status = DecopInteger(client, name + ':tc-status')
        self._tc_status_txt = DecopString(client, name + ':tc-status-txt')
        self._error_code = DecopInteger(client, name + ':error-code')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._power_set = MutableDecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_max = DecopReal(client, name + ':current-max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def tc_status(self) -> 'DecopInteger':
        return self._tc_status

    @property
    def tc_status_txt(self) -> 'DecopString':
        return self._tc_status_txt

    @property
    def error_code(self) -> 'DecopInteger':
        return self._error_code

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def power_set(self) -> 'MutableDecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max


class Scan073790A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._signal_type = MutableDecopInteger(client, name + ':signal-type')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._unit = DecopString(client, name + ':unit')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')
        self._start = MutableDecopReal(client, name + ':start')
        self._end = MutableDecopReal(client, name + ':end')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def signal_type(self) -> 'MutableDecopInteger':
        return self._signal_type

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset

    @property
    def start(self) -> 'MutableDecopReal':
        return self._start

    @property
    def end(self) -> 'MutableDecopReal':
        return self._end


class WideScan06E794C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._scan_begin = MutableDecopReal(client, name + ':scan-begin')
        self._scan_end = MutableDecopReal(client, name + ':scan-end')
        self._continuous_mode = MutableDecopBoolean(client, name + ':continuous-mode')
        self._shape = MutableDecopInteger(client, name + ':shape')
        self._offset = MutableDecopReal(client, name + ':offset')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._speed = MutableDecopReal(client, name + ':speed')
        self._speed_min = DecopReal(client, name + ':speed-min')
        self._speed_max = DecopReal(client, name + ':speed-max')
        self._duration = MutableDecopReal(client, name + ':duration')
        self._value_set = MutableDecopReal(client, name + ':value-set')
        self._value_act = DecopReal(client, name + ':value-act')
        self._value_unit = DecopString(client, name + ':value-unit')
        self._recorder_stepsize_set = MutableDecopReal(client, name + ':recorder-stepsize-set')
        self._recorder_stepsize = DecopReal(client, name + ':recorder-stepsize')
        self._progress = DecopInteger(client, name + ':progress')
        self._remaining_time = DecopInteger(client, name + ':remaining-time')
        self._trigger = Trigger06E79580(client, name + ':trigger')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def scan_begin(self) -> 'MutableDecopReal':
        return self._scan_begin

    @property
    def scan_end(self) -> 'MutableDecopReal':
        return self._scan_end

    @property
    def continuous_mode(self) -> 'MutableDecopBoolean':
        return self._continuous_mode

    @property
    def shape(self) -> 'MutableDecopInteger':
        return self._shape

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def speed(self) -> 'MutableDecopReal':
        return self._speed

    @property
    def speed_min(self) -> 'DecopReal':
        return self._speed_min

    @property
    def speed_max(self) -> 'DecopReal':
        return self._speed_max

    @property
    def duration(self) -> 'MutableDecopReal':
        return self._duration

    @property
    def value_set(self) -> 'MutableDecopReal':
        return self._value_set

    @property
    def value_act(self) -> 'DecopReal':
        return self._value_act

    @property
    def value_unit(self) -> 'DecopString':
        return self._value_unit

    @property
    def recorder_stepsize_set(self) -> 'MutableDecopReal':
        return self._recorder_stepsize_set

    @property
    def recorder_stepsize(self) -> 'DecopReal':
        return self._recorder_stepsize

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def remaining_time(self) -> 'DecopInteger':
        return self._remaining_time

    @property
    def trigger(self) -> 'Trigger06E79580':
        return self._trigger

    def start(self) -> None:
        self.__client.exec(self.__name + ':start', input_stream=None, output_type=None, return_type=None)

    def stop(self) -> None:
        self.__client.exec(self.__name + ':stop', input_stream=None, output_type=None, return_type=None)

    def set_output_to_zoom_offset(self) -> None:
        self.__client.exec(self.__name + ':set-output-to-zoom-offset', input_stream=None, output_type=None, return_type=None)

    def set_scan_range_to_zoom_range(self) -> None:
        self.__client.exec(self.__name + ':set-scan-range-to-zoom-range', input_stream=None, output_type=None, return_type=None)

    def set_zoom_range_to_scan_range(self) -> None:
        self.__client.exec(self.__name + ':set-zoom-range-to-scan-range', input_stream=None, output_type=None, return_type=None)


class Trigger06E79580:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_enabled = MutableDecopBoolean(client, name + ':input-enabled')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._output_enabled = MutableDecopBoolean(client, name + ':output-enabled')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._output_threshold = MutableDecopReal(client, name + ':output-threshold')

    @property
    def input_enabled(self) -> 'MutableDecopBoolean':
        return self._input_enabled

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def output_enabled(self) -> 'MutableDecopBoolean':
        return self._output_enabled

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def output_threshold(self) -> 'MutableDecopReal':
        return self._output_threshold


class Scope06E78800:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel106E78D40(client, name + ':channel1')
        self._channel2 = Channel206E78C20(client, name + ':channel2')
        self._channelx = Channelx06E788C0(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel106E78D40':
        return self._channel1

    @property
    def channel2(self) -> 'Channel206E78C20':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx06E788C0':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel106E78D40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel206E78C20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx06E788C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Recorder06E789E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._inputs = Inputs06E78Aa0(client, name + ':inputs')
        self._recording_mode = MutableDecopInteger(client, name + ':recording-mode')
        self._recording_time = MutableDecopReal(client, name + ':recording-time')
        self._sample_count_set = MutableDecopInteger(client, name + ':sample-count-set')
        self._sample_count = DecopInteger(client, name + ':sample-count')
        self._sampling_interval = DecopReal(client, name + ':sampling-interval')
        self._sampling_rate = DecopReal(client, name + ':sampling-rate')
        self._memory_size = DecopInteger(client, name + ':memory-size')
        self._data = Data06E78Fe0(client, name + ':data')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def inputs(self) -> 'Inputs06E78Aa0':
        return self._inputs

    @property
    def recording_mode(self) -> 'MutableDecopInteger':
        return self._recording_mode

    @property
    def recording_time(self) -> 'MutableDecopReal':
        return self._recording_time

    @property
    def sample_count_set(self) -> 'MutableDecopInteger':
        return self._sample_count_set

    @property
    def sample_count(self) -> 'DecopInteger':
        return self._sample_count

    @property
    def sampling_interval(self) -> 'DecopReal':
        return self._sampling_interval

    @property
    def sampling_rate(self) -> 'DecopReal':
        return self._sampling_rate

    @property
    def memory_size(self) -> 'DecopInteger':
        return self._memory_size

    @property
    def data(self) -> 'Data06E78Fe0':
        return self._data


class Inputs06E78Aa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._channel1 = Channel106E786E0(client, name + ':channel1')
        self._channel2 = Channel206E78B60(client, name + ':channel2')
        self._channelx = Channelx06E78Da0(client, name + ':channelx')

    @property
    def channel1(self) -> 'Channel106E786E0':
        return self._channel1

    @property
    def channel2(self) -> 'Channel206E78B60':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx06E78Da0':
        return self._channelx


class Channel106E786E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._low_pass_filter = LowPassFilter06E78920(client, name + ':low-pass-filter')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def low_pass_filter(self) -> 'LowPassFilter06E78920':
        return self._low_pass_filter


class LowPassFilter06E78920:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._cut_off_frequency = MutableDecopReal(client, name + ':cut-off-frequency')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def cut_off_frequency(self) -> 'MutableDecopReal':
        return self._cut_off_frequency


class Channel206E78B60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._low_pass_filter = LowPassFilter06E791C0(client, name + ':low-pass-filter')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def low_pass_filter(self) -> 'LowPassFilter06E791C0':
        return self._low_pass_filter


class LowPassFilter06E791C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._cut_off_frequency = MutableDecopReal(client, name + ':cut-off-frequency')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def cut_off_frequency(self) -> 'MutableDecopReal':
        return self._cut_off_frequency


class Channelx06E78Da0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal


class Data06E78Fe0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._channel1 = Channel106E79040(client, name + ':channel1')
        self._channel2 = Channel206E78740(client, name + ':channel2')
        self._channelx = Channelx06E790A0(client, name + ':channelx')
        self._zoom_data = DecopBinary(client, name + ':zoom-data')
        self._zoom_offset = MutableDecopReal(client, name + ':zoom-offset')
        self._zoom_amplitude = MutableDecopReal(client, name + ':zoom-amplitude')
        self._recorded_sampling_interval = DecopReal(client, name + ':recorded-sampling-interval')
        self._recorded_sample_count = DecopInteger(client, name + ':recorded-sample-count')
        self._last_recorded_sample = DecopInteger(client, name + ':last-recorded-sample')
        self._last_valid_sample = DecopInteger(client, name + ':last-valid-sample')

    @property
    def channel1(self) -> 'Channel106E79040':
        return self._channel1

    @property
    def channel2(self) -> 'Channel206E78740':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx06E790A0':
        return self._channelx

    @property
    def zoom_data(self) -> 'DecopBinary':
        return self._zoom_data

    @property
    def zoom_offset(self) -> 'MutableDecopReal':
        return self._zoom_offset

    @property
    def zoom_amplitude(self) -> 'MutableDecopReal':
        return self._zoom_amplitude

    @property
    def recorded_sampling_interval(self) -> 'DecopReal':
        return self._recorded_sampling_interval

    @property
    def recorded_sample_count(self) -> 'DecopInteger':
        return self._recorded_sample_count

    @property
    def last_recorded_sample(self) -> 'DecopInteger':
        return self._last_recorded_sample

    @property
    def last_valid_sample(self) -> 'DecopInteger':
        return self._last_valid_sample

    def zoom_out(self) -> None:
        self.__client.exec(self.__name + ':zoom-out', input_stream=None, output_type=None, return_type=None)

    def get_data(self) -> None:
        self.__client.exec(self.__name + ':get-data', input_stream=None, output_type=None, return_type=None)

    def show_data(self) -> None:
        self.__client.exec(self.__name + ':show-data', input_stream=None, output_type=None, return_type=None)


class Channel106E79040:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel206E78740:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx06E790A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Nlo06E79220:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._servo = Servo06E787A0(client, name + ':servo')
        self._pd = Pd06E84F38(client, name + ':pd')
        self._power_optimization = PowerOptimization06E874C8(client, name + ':power-optimization')
        self._auto_nlo = AutoNlo071D8080(client, name + ':auto-nlo')
        self._shg = Shg071D82C0(client, name + ':shg')
        self._fhg = Fhg071E31B8(client, name + ':fhg')
        self._ssw_ver = DecopString(client, name + ':ssw-ver')

    @property
    def servo(self) -> 'Servo06E787A0':
        return self._servo

    @property
    def pd(self) -> 'Pd06E84F38':
        return self._pd

    @property
    def power_optimization(self) -> 'PowerOptimization06E874C8':
        return self._power_optimization

    @property
    def auto_nlo(self) -> 'AutoNlo071D8080':
        return self._auto_nlo

    @property
    def shg(self) -> 'Shg071D82C0':
        return self._shg

    @property
    def fhg(self) -> 'Fhg071E31B8':
        return self._fhg

    @property
    def ssw_ver(self) -> 'DecopString':
        return self._ssw_ver


class Servo06E787A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ta1_hor = Ta1Hor06E843F8(client, name + ':ta1-hor')
        self._ta1_vert = Ta1Vert06E84158(client, name + ':ta1-vert')
        self._ta2_hor = Ta2Hor06E846F8(client, name + ':ta2-hor')
        self._ta2_vert = Ta2Vert06E849F8(client, name + ':ta2-vert')
        self._shg1_hor = Shg1Hor06E84098(client, name + ':shg1-hor')
        self._shg1_vert = Shg1Vert06E841B8(client, name + ':shg1-vert')
        self._shg2_hor = Shg2Hor06E84A58(client, name + ':shg2-hor')
        self._shg2_vert = Shg2Vert06E84638(client, name + ':shg2-vert')
        self._fhg1_hor = Fhg1Hor06E84B18(client, name + ':fhg1-hor')
        self._fhg1_vert = Fhg1Vert06E84B78(client, name + ':fhg1-vert')
        self._fhg2_hor = Fhg2Hor06E842D8(client, name + ':fhg2-hor')
        self._fhg2_vert = Fhg2Vert06E84Bd8(client, name + ':fhg2-vert')
        self._fiber1_hor = Fiber1Hor06E84998(client, name + ':fiber1-hor')
        self._fiber1_vert = Fiber1Vert06E84398(client, name + ':fiber1-vert')
        self._fiber2_hor = Fiber2Hor06E84458(client, name + ':fiber2-hor')
        self._fiber2_vert = Fiber2Vert06E840F8(client, name + ':fiber2-vert')
        self._uv_outcpl = UvOutcpl06E84Ed8(client, name + ':uv-outcpl')
        self._uv_cryst = UvCryst06E84C98(client, name + ':uv-cryst')

    @property
    def ta1_hor(self) -> 'Ta1Hor06E843F8':
        return self._ta1_hor

    @property
    def ta1_vert(self) -> 'Ta1Vert06E84158':
        return self._ta1_vert

    @property
    def ta2_hor(self) -> 'Ta2Hor06E846F8':
        return self._ta2_hor

    @property
    def ta2_vert(self) -> 'Ta2Vert06E849F8':
        return self._ta2_vert

    @property
    def shg1_hor(self) -> 'Shg1Hor06E84098':
        return self._shg1_hor

    @property
    def shg1_vert(self) -> 'Shg1Vert06E841B8':
        return self._shg1_vert

    @property
    def shg2_hor(self) -> 'Shg2Hor06E84A58':
        return self._shg2_hor

    @property
    def shg2_vert(self) -> 'Shg2Vert06E84638':
        return self._shg2_vert

    @property
    def fhg1_hor(self) -> 'Fhg1Hor06E84B18':
        return self._fhg1_hor

    @property
    def fhg1_vert(self) -> 'Fhg1Vert06E84B78':
        return self._fhg1_vert

    @property
    def fhg2_hor(self) -> 'Fhg2Hor06E842D8':
        return self._fhg2_hor

    @property
    def fhg2_vert(self) -> 'Fhg2Vert06E84Bd8':
        return self._fhg2_vert

    @property
    def fiber1_hor(self) -> 'Fiber1Hor06E84998':
        return self._fiber1_hor

    @property
    def fiber1_vert(self) -> 'Fiber1Vert06E84398':
        return self._fiber1_vert

    @property
    def fiber2_hor(self) -> 'Fiber2Hor06E84458':
        return self._fiber2_hor

    @property
    def fiber2_vert(self) -> 'Fiber2Vert06E840F8':
        return self._fiber2_vert

    @property
    def uv_outcpl(self) -> 'UvOutcpl06E84Ed8':
        return self._uv_outcpl

    @property
    def uv_cryst(self) -> 'UvCryst06E84C98':
        return self._uv_cryst


class Ta1Hor06E843F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta1Vert06E84158:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta2Hor06E846F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta2Vert06E849F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg1Hor06E84098:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg1Vert06E841B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg2Hor06E84A58:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg2Vert06E84638:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg1Hor06E84B18:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg1Vert06E84B78:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg2Hor06E842D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg2Vert06E84Bd8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber1Hor06E84998:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber1Vert06E84398:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber2Hor06E84458:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber2Vert06E840F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class UvOutcpl06E84Ed8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class UvCryst06E84C98:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Pd06E84F38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._dl = Dl06E84C38(client, name + ':dl')
        self._amp = Amp06E84Db8(client, name + ':amp')
        self._fiber = Fiber06E84Cf8(client, name + ':fiber')
        self._shg = Shg06E87468(client, name + ':shg')
        self._shg_input = ShgInput06E87288(client, name + ':shg-input')
        self._shg_int = ShgInt06E870A8(client, name + ':shg-int')
        self._shg_pdh_dc = ShgPdhDc06E87708(client, name + ':shg-pdh-dc')
        self._shg_pdh_rf = ShgPdhRf06E87828(client, name + ':shg-pdh-rf')
        self._fhg = Fhg06E87048(client, name + ':fhg')
        self._fhg_int = FhgInt06E87Be8(client, name + ':fhg-int')
        self._fhg_pdh_dc = FhgPdhDc06E871C8(client, name + ':fhg-pdh-dc')
        self._fhg_pdh_rf = FhgPdhRf06E87768(client, name + ':fhg-pdh-rf')

    @property
    def dl(self) -> 'Dl06E84C38':
        return self._dl

    @property
    def amp(self) -> 'Amp06E84Db8':
        return self._amp

    @property
    def fiber(self) -> 'Fiber06E84Cf8':
        return self._fiber

    @property
    def shg(self) -> 'Shg06E87468':
        return self._shg

    @property
    def shg_input(self) -> 'ShgInput06E87288':
        return self._shg_input

    @property
    def shg_int(self) -> 'ShgInt06E870A8':
        return self._shg_int

    @property
    def shg_pdh_dc(self) -> 'ShgPdhDc06E87708':
        return self._shg_pdh_dc

    @property
    def shg_pdh_rf(self) -> 'ShgPdhRf06E87828':
        return self._shg_pdh_rf

    @property
    def fhg(self) -> 'Fhg06E87048':
        return self._fhg

    @property
    def fhg_int(self) -> 'FhgInt06E87Be8':
        return self._fhg_int

    @property
    def fhg_pdh_dc(self) -> 'FhgPdhDc06E871C8':
        return self._fhg_pdh_dc

    @property
    def fhg_pdh_rf(self) -> 'FhgPdhRf06E87768':
        return self._fhg_pdh_rf


class Dl06E84C38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp06E84Db8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Fiber06E84Cf8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Shg06E87468:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInput06E87288:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInt06E870A8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class ShgPdhDc06E87708:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class ShgPdhRf06E87828:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = MutableDecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'MutableDecopReal':
        return self._gain


class Fhg06E87048:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class FhgInt06E87Be8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class FhgPdhDc06E871C8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class FhgPdhRf06E87768:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = MutableDecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'MutableDecopReal':
        return self._gain


class PowerOptimization06E874C8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ongoing = DecopBoolean(client, name + ':ongoing')
        self._progress = DecopInteger(client, name + ':progress')
        self._status = DecopInteger(client, name + ':status')
        self._status_string = DecopString(client, name + ':status-string')
        self._shg_advanced = MutableDecopBoolean(client, name + ':shg-advanced')
        self._stage1 = Stage106E87528(client, name + ':stage1')
        self._stage2 = Stage206E87A08(client, name + ':stage2')
        self._stage3 = Stage306E87348(client, name + ':stage3')
        self._stage4 = Stage406E87F48(client, name + ':stage4')
        self._stage5 = Stage506E87Dc8(client, name + ':stage5')
        self._progress_data_amp = DecopBinary(client, name + ':progress-data-amp')
        self._progress_data_shg = DecopBinary(client, name + ':progress-data-shg')
        self._progress_data_fiber = DecopBinary(client, name + ':progress-data-fiber')
        self._progress_data_fhg = DecopBinary(client, name + ':progress-data-fhg')
        self._abort = MutableDecopBoolean(client, name + ':abort')

    @property
    def ongoing(self) -> 'DecopBoolean':
        return self._ongoing

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_string(self) -> 'DecopString':
        return self._status_string

    @property
    def shg_advanced(self) -> 'MutableDecopBoolean':
        return self._shg_advanced

    @property
    def stage1(self) -> 'Stage106E87528':
        return self._stage1

    @property
    def stage2(self) -> 'Stage206E87A08':
        return self._stage2

    @property
    def stage3(self) -> 'Stage306E87348':
        return self._stage3

    @property
    def stage4(self) -> 'Stage406E87F48':
        return self._stage4

    @property
    def stage5(self) -> 'Stage506E87Dc8':
        return self._stage5

    @property
    def progress_data_amp(self) -> 'DecopBinary':
        return self._progress_data_amp

    @property
    def progress_data_shg(self) -> 'DecopBinary':
        return self._progress_data_shg

    @property
    def progress_data_fiber(self) -> 'DecopBinary':
        return self._progress_data_fiber

    @property
    def progress_data_fhg(self) -> 'DecopBinary':
        return self._progress_data_fhg

    @property
    def abort(self) -> 'MutableDecopBoolean':
        return self._abort

    def start_optimization_all(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-all', input_stream=None, output_type=None, return_type=None)

    def start_optimization_amp(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-amp', input_stream=None, output_type=None, return_type=None)

    def start_optimization_shg(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-shg', input_stream=None, output_type=None, return_type=None)

    def start_optimization_fiber(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-fiber', input_stream=None, output_type=None, return_type=None)

    def start_optimization_fhg(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-fhg', input_stream=None, output_type=None, return_type=None)


class Stage106E87528:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input06E87948(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input06E87948':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input06E87948:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage206E87A08:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input06E87A68(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input06E87A68':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input06E87A68:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage306E87348:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input06E873A8(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input06E873A8':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input06E873A8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage406E87F48:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input06E87C48(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input06E87C48':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input06E87C48:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage506E87Dc8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input06E87D68(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input06E87D68':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input06E87D68:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class AutoNlo071D8080:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._automatic_mode = DecopBoolean(client, name + ':automatic-mode')
        self._laser_on = MutableDecopBoolean(client, name + ':laser-on')
        self._emission = DecopBoolean(client, name + ':emission')
        self._operation_time_master = DecopReal(client, name + ':operation-time-master')
        self._operation_time_amplifier = DecopReal(client, name + ':operation-time-amplifier')
        self._operation_time_cavity = DecopReal(client, name + ':operation-time-cavity')
        self._amplifier_current_margin = DecopReal(client, name + ':amplifier-current-margin')

    @property
    def automatic_mode(self) -> 'DecopBoolean':
        return self._automatic_mode

    @property
    def laser_on(self) -> 'MutableDecopBoolean':
        return self._laser_on

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def operation_time_master(self) -> 'DecopReal':
        return self._operation_time_master

    @property
    def operation_time_amplifier(self) -> 'DecopReal':
        return self._operation_time_amplifier

    @property
    def operation_time_cavity(self) -> 'DecopReal':
        return self._operation_time_cavity

    @property
    def amplifier_current_margin(self) -> 'DecopReal':
        return self._amplifier_current_margin

    def perform_single_mode_optimization(self) -> None:
        self.__client.exec(self.__name + ':perform-single-mode-optimization', input_stream=None, output_type=None, return_type=None)

    def perform_auto_align(self) -> None:
        self.__client.exec(self.__name + ':perform-auto-align', input_stream=None, output_type=None, return_type=None)


class Shg071D82C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071D8140(client, name + ':tc')
        self._pc = Pc071D85C0(client, name + ':pc')
        self._scan = Scan071D8Bc0(client, name + ':scan')
        self._scope = Scope071D8800(client, name + ':scope')
        self._lock = Lock071D8D40(client, name + ':lock')
        self._factory_settings = FactorySettings071E37B8(client, name + ':factory-settings')

    @property
    def tc(self) -> 'Tc071D8140':
        return self._tc

    @property
    def pc(self) -> 'Pc071D85C0':
        return self._pc

    @property
    def scan(self) -> 'Scan071D8Bc0':
        return self._scan

    @property
    def scope(self) -> 'Scope071D8800':
        return self._scope

    @property
    def lock(self) -> 'Lock071D8D40':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings071E37B8':
        return self._factory_settings


class Tc071D8140:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput071D8980(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop071D8860(client, name + ':t-loop')
        self._limits = Limits071D89E0(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput071D8980':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop071D8860':
        return self._t_loop

    @property
    def limits(self) -> 'Limits071D89E0':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput071D8980:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop071D8860:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits071D89E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc071D85C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput071D8380(client, name + ':external-input')
        self._output_filter = OutputFilter071D87A0(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput071D8380':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter071D87A0':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput071D8380:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter071D87A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Scan071D8Bc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset


class Scope071D8800:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel1071D80E0(client, name + ':channel1')
        self._channel2 = Channel2071D81A0(client, name + ':channel2')
        self._channelx = Channelx071D8500(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel1071D80E0':
        return self._channel1

    @property
    def channel2(self) -> 'Channel2071D81A0':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx071D8500':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel1071D80E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel2071D81A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx071D8500:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock071D8D40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock071D8Fe0(client, name + ':relock')
        self._window = Window071D8C80(client, name + ':window')
        self._pid1 = Pid1071D8E00(client, name + ':pid1')
        self._pid2 = Pid2071D8Ec0(client, name + ':pid2')
        self._analog_dl_gain = AnalogDlGain071E3Ab8(client, name + ':analog-dl-gain')
        self._local_oscillator = LocalOscillator071E30F8(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = MutableDecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = MutableDecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock071D8Fe0':
        return self._relock

    @property
    def window(self) -> 'Window071D8C80':
        return self._window

    @property
    def pid1(self) -> 'Pid1071D8E00':
        return self._pid1

    @property
    def pid2(self) -> 'Pid2071D8Ec0':
        return self._pid2

    @property
    def analog_dl_gain(self) -> 'AnalogDlGain071E3Ab8':
        return self._analog_dl_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator071E30F8':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock071D8Fe0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Window071D8C80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._threshold = MutableDecopReal(client, name + ':threshold')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration071D8Ce0(client, name + ':calibration')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'MutableDecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration071D8Ce0':
        return self._calibration


class Calibration071D8Ce0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid1071D8E00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain071D8F20(client, name + ':gain')

    @property
    def gain(self) -> 'Gain071D8F20':
        return self._gain


class Gain071D8F20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class Pid2071D8Ec0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain071D8F80(client, name + ':gain')

    @property
    def gain(self) -> 'Gain071D8F80':
        return self._gain


class Gain071D8F80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class AnalogDlGain071E3Ab8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain


class LocalOscillator071E30F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._use_external_oscillator = MutableDecopBoolean(client, name + ':use-external-oscillator')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._attenuation_raw = MutableDecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def use_external_oscillator(self) -> 'MutableDecopBoolean':
        return self._use_external_oscillator

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'MutableDecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    def auto_pdh(self) -> None:
        self.__client.exec(self.__name + ':auto-pdh', input_stream=None, output_type=None, return_type=None)


class FactorySettings071E37B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071E3758(client, name + ':tc')
        self._pc = Pc071E3638(client, name + ':pc')
        self._pd = Pd071E3938(client, name + ':pd')
        self._lock = Lock071E3578(client, name + ':lock')

    @property
    def tc(self) -> 'Tc071E3758':
        return self._tc

    @property
    def pc(self) -> 'Pc071E3638':
        return self._pc

    @property
    def pd(self) -> 'Pd071E3938':
        return self._pd

    @property
    def lock(self) -> 'Lock071E3578':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Tc071E3758:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc071E3638:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd071E3938:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg071E3698(client, name + ':shg')
        self._shg_input = ShgInput071E3098(client, name + ':shg-input')
        self._fiber = Fiber071E33F8(client, name + ':fiber')
        self._int = Int071E32D8(client, name + ':int')
        self._pdh_dc = PdhDc071E3458(client, name + ':pdh-dc')
        self._pdh_rf = PdhRf071E38D8(client, name + ':pdh-rf')

    @property
    def shg(self) -> 'Shg071E3698':
        return self._shg

    @property
    def shg_input(self) -> 'ShgInput071E3098':
        return self._shg_input

    @property
    def fiber(self) -> 'Fiber071E33F8':
        return self._fiber

    @property
    def int(self) -> 'Int071E32D8':
        return self._int

    @property
    def pdh_dc(self) -> 'PdhDc071E3458':
        return self._pdh_dc

    @property
    def pdh_rf(self) -> 'PdhRf071E38D8':
        return self._pdh_rf


class Shg071E3698:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInput071E3098:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Fiber071E33F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Int071E32D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhDc071E3458:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhRf071E38D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class Lock071E3578:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock071E3B78(client, name + ':relock')
        self._window = Window071E3158(client, name + ':window')
        self._pid1_gain = Pid1Gain071E34B8(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain071E36F8(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator071E3A58(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock071E3B78':
        return self._relock

    @property
    def window(self) -> 'Window071E3158':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain071E34B8':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain071E36F8':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator071E3A58':
        return self._local_oscillator


class Relock071E3B78:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window071E3158:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain071E34B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain071E36F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator071E3A58:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class Fhg071E31B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071E39F8(client, name + ':tc')
        self._pc = Pc071E47D8(client, name + ':pc')
        self._scan = Scan071E3D58(client, name + ':scan')
        self._scope = Scope071E4838(client, name + ':scope')
        self._lock = Lock071E4118(client, name + ':lock')
        self._factory_settings = FactorySettings071E4E98(client, name + ':factory-settings')

    @property
    def tc(self) -> 'Tc071E39F8':
        return self._tc

    @property
    def pc(self) -> 'Pc071E47D8':
        return self._pc

    @property
    def scan(self) -> 'Scan071E3D58':
        return self._scan

    @property
    def scope(self) -> 'Scope071E4838':
        return self._scope

    @property
    def lock(self) -> 'Lock071E4118':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings071E4E98':
        return self._factory_settings


class Tc071E39F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput071E3218(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop071E3278(client, name + ':t-loop')
        self._limits = Limits071E4178(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput071E3218':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop071E3278':
        return self._t_loop

    @property
    def limits(self) -> 'Limits071E4178':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput071E3218:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop071E3278:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits071E4178:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc071E47D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput071E3Ff8(client, name + ':external-input')
        self._output_filter = OutputFilter071E4658(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput071E3Ff8':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter071E4658':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput071E3Ff8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter071E4658:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Scan071E3D58:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset


class Scope071E4838:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel1071E3F98(client, name + ':channel1')
        self._channel2 = Channel2071E40B8(client, name + ':channel2')
        self._channelx = Channelx071E42F8(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel1071E3F98':
        return self._channel1

    @property
    def channel2(self) -> 'Channel2071E40B8':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx071E42F8':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel1071E3F98:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel2071E40B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx071E42F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock071E4118:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock071E46B8(client, name + ':relock')
        self._window = Window071E4298(client, name + ':window')
        self._pid1 = Pid1071E4478(client, name + ':pid1')
        self._pid2 = Pid2071E4538(client, name + ':pid2')
        self._local_oscillator = LocalOscillator071E45F8(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = MutableDecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = MutableDecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock071E46B8':
        return self._relock

    @property
    def window(self) -> 'Window071E4298':
        return self._window

    @property
    def pid1(self) -> 'Pid1071E4478':
        return self._pid1

    @property
    def pid2(self) -> 'Pid2071E4538':
        return self._pid2

    @property
    def local_oscillator(self) -> 'LocalOscillator071E45F8':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock071E46B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Window071E4298:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._threshold = MutableDecopReal(client, name + ':threshold')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration071E4418(client, name + ':calibration')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'MutableDecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration071E4418':
        return self._calibration


class Calibration071E4418:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid1071E4478:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain071E44D8(client, name + ':gain')

    @property
    def gain(self) -> 'Gain071E44D8':
        return self._gain


class Gain071E44D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class Pid2071E4538:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain071E4598(client, name + ':gain')

    @property
    def gain(self) -> 'Gain071E4598':
        return self._gain


class Gain071E4598:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator071E45F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._attenuation_raw = MutableDecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'MutableDecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    def auto_pdh(self) -> None:
        self.__client.exec(self.__name + ':auto-pdh', input_stream=None, output_type=None, return_type=None)


class FactorySettings071E4E98:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071E4Bf8(client, name + ':tc')
        self._pc = Pc071E4E38(client, name + ':pc')
        self._pd = Pd071E4A78(client, name + ':pd')
        self._lock = Lock071E49B8(client, name + ':lock')

    @property
    def tc(self) -> 'Tc071E4Bf8':
        return self._tc

    @property
    def pc(self) -> 'Pc071E4E38':
        return self._pc

    @property
    def pd(self) -> 'Pd071E4A78':
        return self._pd

    @property
    def lock(self) -> 'Lock071E49B8':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Tc071E4Bf8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc071E4E38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd071E4A78:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._fhg = Fhg071E4Ef8(client, name + ':fhg')
        self._int = Int071E4898(client, name + ':int')
        self._pdh_dc = PdhDc071E4B38(client, name + ':pdh-dc')
        self._pdh_rf = PdhRf071E4Cb8(client, name + ':pdh-rf')

    @property
    def fhg(self) -> 'Fhg071E4Ef8':
        return self._fhg

    @property
    def int(self) -> 'Int071E4898':
        return self._int

    @property
    def pdh_dc(self) -> 'PdhDc071E4B38':
        return self._pdh_dc

    @property
    def pdh_rf(self) -> 'PdhRf071E4Cb8':
        return self._pdh_rf


class Fhg071E4Ef8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Int071E4898:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhDc071E4B38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhRf071E4Cb8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class Lock071E49B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock071E4Fb8(client, name + ':relock')
        self._window = Window071E4D18(client, name + ':window')
        self._pid1_gain = Pid1Gain071E48F8(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain071E4A18(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator071E4Ad8(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock071E4Fb8':
        return self._relock

    @property
    def window(self) -> 'Window071E4D18':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain071E48F8':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain071E4A18':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator071E4Ad8':
        return self._local_oscillator


class Relock071E4Fb8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window071E4D18:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain071E48F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain071E4A18:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator071E4Ad8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class Uv071Eceb8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pump = Pump071Ed3F8(client, name + ':pump')
        self._eom = Eom071Ec9D8(client, name + ':eom')
        self._cavity = Cavity071Ed158(client, name + ':cavity')
        self._crystal = Crystal071Ed5D8(client, name + ':crystal')
        self._servo = Servo071Eded8(client, name + ':servo')
        self._pd = Pd071Ee478(client, name + ':pd')
        self._power_optimization = PowerOptimization071Ee4D8(client, name + ':power-optimization')
        self._power_stabilization = PowerStabilization071Ee658(client, name + ':power-stabilization')
        self._scan = Scan071Ee6B8(client, name + ':scan')
        self._scope = Scope071Ee718(client, name + ':scope')
        self._lock = Lock074084E0(client, name + ':lock')
        self._factory_settings = FactorySettings074086C0(client, name + ':factory-settings')
        self._status_parameters = StatusParameters07408C60(client, name + ':status-parameters')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._hwp_transmittance = DecopReal(client, name + ':hwp-transmittance')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._specs_fulfilled = DecopBoolean(client, name + ':specs-fulfilled')
        self._error = DecopInteger(client, name + ':error')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._remaining_optics_spots = DecopInteger(client, name + ':remaining-optics-spots')
        self._baseplate_temperature = DecopReal(client, name + ':baseplate-temperature')
        self._ssw_ver = DecopString(client, name + ':ssw-ver')

    @property
    def pump(self) -> 'Pump071Ed3F8':
        return self._pump

    @property
    def eom(self) -> 'Eom071Ec9D8':
        return self._eom

    @property
    def cavity(self) -> 'Cavity071Ed158':
        return self._cavity

    @property
    def crystal(self) -> 'Crystal071Ed5D8':
        return self._crystal

    @property
    def servo(self) -> 'Servo071Eded8':
        return self._servo

    @property
    def pd(self) -> 'Pd071Ee478':
        return self._pd

    @property
    def power_optimization(self) -> 'PowerOptimization071Ee4D8':
        return self._power_optimization

    @property
    def power_stabilization(self) -> 'PowerStabilization071Ee658':
        return self._power_stabilization

    @property
    def scan(self) -> 'Scan071Ee6B8':
        return self._scan

    @property
    def scope(self) -> 'Scope071Ee718':
        return self._scope

    @property
    def lock(self) -> 'Lock074084E0':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings074086C0':
        return self._factory_settings

    @property
    def status_parameters(self) -> 'StatusParameters07408C60':
        return self._status_parameters

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def hwp_transmittance(self) -> 'DecopReal':
        return self._hwp_transmittance

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def specs_fulfilled(self) -> 'DecopBoolean':
        return self._specs_fulfilled

    @property
    def error(self) -> 'DecopInteger':
        return self._error

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def remaining_optics_spots(self) -> 'DecopInteger':
        return self._remaining_optics_spots

    @property
    def baseplate_temperature(self) -> 'DecopReal':
        return self._baseplate_temperature

    @property
    def ssw_ver(self) -> 'DecopString':
        return self._ssw_ver

    def perform_optimization(self) -> None:
        self.__client.exec(self.__name + ':perform-optimization', input_stream=None, output_type=None, return_type=None)

    def perform_optics_shift(self) -> None:
        self.__client.exec(self.__name + ':perform-optics-shift', input_stream=None, output_type=None, return_type=None)

    def clear_errors(self) -> None:
        self.__client.exec(self.__name + ':clear-errors', input_stream=None, output_type=None, return_type=None)


class Pump071Ed3F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._tc_status = DecopInteger(client, name + ':tc-status')
        self._tc_status_txt = DecopString(client, name + ':tc-status-txt')
        self._error_code = DecopInteger(client, name + ':error-code')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._power_set = DecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_max = DecopReal(client, name + ':current-max')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def tc_status(self) -> 'DecopInteger':
        return self._tc_status

    @property
    def tc_status_txt(self) -> 'DecopString':
        return self._tc_status_txt

    @property
    def error_code(self) -> 'DecopInteger':
        return self._error_code

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def power_set(self) -> 'DecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max


class Eom071Ec9D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071Ecbb8(client, name + ':tc')

    @property
    def tc(self) -> 'Tc071Ecbb8':
        return self._tc


class Tc071Ecbb8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput071Ece58(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop071Ed038(client, name + ':t-loop')
        self._limits = Limits071Ed518(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput071Ece58':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop071Ed038':
        return self._t_loop

    @property
    def limits(self) -> 'Limits071Ed518':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput071Ece58:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop071Ed038:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits071Ed518:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Cavity071Ed158:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071Ed398(client, name + ':tc')
        self._pc = Pc071Ed098(client, name + ':pc')

    @property
    def tc(self) -> 'Tc071Ed398':
        return self._tc

    @property
    def pc(self) -> 'Pc071Ed098':
        return self._pc


class Tc071Ed398:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput071Ecaf8(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop071Eccd8(client, name + ':t-loop')
        self._limits = Limits071Ecf78(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput071Ecaf8':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop071Eccd8':
        return self._t_loop

    @property
    def limits(self) -> 'Limits071Ecf78':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput071Ecaf8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop071Eccd8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits071Ecf78:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc071Ed098:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._voltage_set = DecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = DecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput071Ed218(client, name + ':external-input')
        self._output_filter = OutputFilter071Ed2D8(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'DecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'DecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput071Ed218':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter071Ed2D8':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput071Ed218:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class OutputFilter071Ed2D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = DecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = DecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'DecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'DecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Crystal071Ed5D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc071Edf38(client, name + ':tc')
        self._optics_shifters = OpticsShifters071Ed998(client, name + ':optics-shifters')

    @property
    def tc(self) -> 'Tc071Edf38':
        return self._tc

    @property
    def optics_shifters(self) -> 'OpticsShifters071Ed998':
        return self._optics_shifters


class Tc071Edf38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput071Ed818(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop071Edf98(client, name + ':t-loop')
        self._limits = Limits071Edd58(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput071Ed818':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop071Edf98':
        return self._t_loop

    @property
    def limits(self) -> 'Limits071Edd58':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput071Ed818:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop071Edf98:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits071Edd58:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class OpticsShifters071Ed998:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._current_spot = DecopInteger(client, name + ':current-spot')
        self._remaining_spots = DecopInteger(client, name + ':remaining-spots')

    @property
    def current_spot(self) -> 'DecopInteger':
        return self._current_spot

    @property
    def remaining_spots(self) -> 'DecopInteger':
        return self._remaining_spots


class Servo071Eded8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg1_hor = Shg1Hor071Ed9F8(client, name + ':shg1-hor')
        self._shg1_vert = Shg1Vert071Ed938(client, name + ':shg1-vert')
        self._shg2_hor = Shg2Hor071Edcf8(client, name + ':shg2-hor')
        self._shg2_vert = Shg2Vert071Ede78(client, name + ':shg2-vert')
        self._hwp = Hwp071Ee058(client, name + ':hwp')
        self._lens = Lens071Ee178(client, name + ':lens')
        self._outcpl = Outcpl071Ee0B8(client, name + ':outcpl')
        self._cryst = Cryst071Ed878(client, name + ':cryst')
        self._comp_hor = CompHor071Edb18(client, name + ':comp-hor')
        self._comp_vert = CompVert071Edc38(client, name + ':comp-vert')

    @property
    def shg1_hor(self) -> 'Shg1Hor071Ed9F8':
        return self._shg1_hor

    @property
    def shg1_vert(self) -> 'Shg1Vert071Ed938':
        return self._shg1_vert

    @property
    def shg2_hor(self) -> 'Shg2Hor071Edcf8':
        return self._shg2_hor

    @property
    def shg2_vert(self) -> 'Shg2Vert071Ede78':
        return self._shg2_vert

    @property
    def hwp(self) -> 'Hwp071Ee058':
        return self._hwp

    @property
    def lens(self) -> 'Lens071Ee178':
        return self._lens

    @property
    def outcpl(self) -> 'Outcpl071Ee0B8':
        return self._outcpl

    @property
    def cryst(self) -> 'Cryst071Ed878':
        return self._cryst

    @property
    def comp_hor(self) -> 'CompHor071Edb18':
        return self._comp_hor

    @property
    def comp_vert(self) -> 'CompVert071Edc38':
        return self._comp_vert


class Shg1Hor071Ed9F8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg1Vert071Ed938:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg2Hor071Edcf8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg2Vert071Ede78:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Hwp071Ee058:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Lens071Ee178:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Outcpl071Ee0B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Cryst071Ed878:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class CompHor071Edb18:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class CompVert071Edc38:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Pd071Ee478:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg071Ee3B8(client, name + ':shg')
        self._pdh_rf = PdhRf071Ee7D8(client, name + ':pdh-rf')
        self._pdh_dc = PdhDc071Ee898(client, name + ':pdh-dc')

    @property
    def shg(self) -> 'Shg071Ee3B8':
        return self._shg

    @property
    def pdh_rf(self) -> 'PdhRf071Ee7D8':
        return self._pdh_rf

    @property
    def pdh_dc(self) -> 'PdhDc071Ee898':
        return self._pdh_dc


class Shg071Ee3B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class PdhRf071Ee7D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = DecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class PdhDc071Ee898:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PowerOptimization071Ee4D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ongoing = DecopBoolean(client, name + ':ongoing')
        self._status = DecopInteger(client, name + ':status')
        self._status_string = DecopString(client, name + ':status-string')
        self._cavity = Cavity071Ee1D8(client, name + ':cavity')
        self._progress_data = DecopBinary(client, name + ':progress-data')
        self._abort = DecopBoolean(client, name + ':abort')

    @property
    def ongoing(self) -> 'DecopBoolean':
        return self._ongoing

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_string(self) -> 'DecopString':
        return self._status_string

    @property
    def cavity(self) -> 'Cavity071Ee1D8':
        return self._cavity

    @property
    def progress_data(self) -> 'DecopBinary':
        return self._progress_data

    @property
    def abort(self) -> 'DecopBoolean':
        return self._abort


class Cavity071Ee1D8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input071Ee778(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = DecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = DecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = DecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input071Ee778':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'DecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'DecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'DecopInteger':
        return self._regress_tolerance


class Input071Ee778:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class PowerStabilization071Ee658:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._gain = Gain071Ee238(client, name + ':gain')
        self._power_set = DecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_max = DecopReal(client, name + ':power-max')
        self._state = DecopInteger(client, name + ':state')
        self._update_strategy = DecopInteger(client, name + ':update-strategy')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain071Ee238':
        return self._gain

    @property
    def power_set(self) -> 'DecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def update_strategy(self) -> 'DecopInteger':
        return self._update_strategy


class Gain071Ee238:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d


class Scan071Ee6B8:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._offset = DecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'DecopReal':
        return self._offset


class Scope071Ee718:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = DecopInteger(client, name + ':variant')
        self._update_rate = DecopInteger(client, name + ':update-rate')
        self._channel1 = Channel107408060(client, name + ':channel1')
        self._channel2 = Channel207408540(client, name + ':channel2')
        self._channelx = Channelx07407Dc0(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'DecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'DecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel107408060':
        return self._channel1

    @property
    def channel2(self) -> 'Channel207408540':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx07407Dc0':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel107408060:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel207408540:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx07407Dc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = DecopInteger(client, name + ':xy-signal')
        self._scope_timescale = DecopReal(client, name + ':scope-timescale')
        self._spectrum_range = DecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = DecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'DecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'DecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'DecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'DecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock074084E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = DecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock07408180(client, name + ':relock')
        self._window = Window07408660(client, name + ':window')
        self._pid1 = Pid1074081E0(client, name + ':pid1')
        self._pid2 = Pid207407Fa0(client, name + ':pid2')
        self._analog_dl_gain = AnalogDlGain07408000(client, name + ':analog-dl-gain')
        self._local_oscillator = LocalOscillator07407E20(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = DecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = DecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'DecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock07408180':
        return self._relock

    @property
    def window(self) -> 'Window07408660':
        return self._window

    @property
    def pid1(self) -> 'Pid1074081E0':
        return self._pid1

    @property
    def pid2(self) -> 'Pid207407Fa0':
        return self._pid2

    @property
    def analog_dl_gain(self) -> 'AnalogDlGain07408000':
        return self._analog_dl_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator07407E20':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'DecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'DecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock07408180:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window07408660:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration07408120(client, name + ':calibration')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration07408120':
        return self._calibration


class Calibration07408120:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid1074081E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain07407Ee0(client, name + ':gain')

    @property
    def gain(self) -> 'Gain07407Ee0':
        return self._gain


class Gain07407Ee0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid207407Fa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain07407F40(client, name + ':gain')

    @property
    def gain(self) -> 'Gain07407F40':
        return self._gain


class Gain07407F40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class AnalogDlGain07408000:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain


class LocalOscillator07407E20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._use_external_oscillator = DecopBoolean(client, name + ':use-external-oscillator')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._attenuation_raw = DecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = DecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def use_external_oscillator(self) -> 'DecopBoolean':
        return self._use_external_oscillator

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'DecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'DecopReal':
        return self._phase_shift


class FactorySettings074086C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._eom_tc = EomTc07408300(client, name + ':eom-tc')
        self._crystal_tc = CrystalTc07407C40(client, name + ':crystal-tc')
        self._cavity_tc = CavityTc07407Ca0(client, name + ':cavity-tc')
        self._pc = Pc07408840(client, name + ':pc')
        self._pd = Pd07408E40(client, name + ':pd')
        self._lock = Lock07408Ae0(client, name + ':lock')

    @property
    def eom_tc(self) -> 'EomTc07408300':
        return self._eom_tc

    @property
    def crystal_tc(self) -> 'CrystalTc07407C40':
        return self._crystal_tc

    @property
    def cavity_tc(self) -> 'CavityTc07407Ca0':
        return self._cavity_tc

    @property
    def pc(self) -> 'Pc07408840':
        return self._pc

    @property
    def pd(self) -> 'Pd07408E40':
        return self._pd

    @property
    def lock(self) -> 'Lock07408Ae0':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class EomTc07408300:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class CrystalTc07407C40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class CavityTc07407Ca0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc07408840:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd07408E40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg074088A0(client, name + ':shg')
        self._pdh_rf = PdhRf07408F60(client, name + ':pdh-rf')
        self._pdh_dc = PdhDc074089C0(client, name + ':pdh-dc')

    @property
    def shg(self) -> 'Shg074088A0':
        return self._shg

    @property
    def pdh_rf(self) -> 'PdhRf07408F60':
        return self._pdh_rf

    @property
    def pdh_dc(self) -> 'PdhDc074089C0':
        return self._pdh_dc


class Shg074088A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class PdhRf07408F60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class PdhDc074089C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class Lock07408Ae0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock07408D80(client, name + ':relock')
        self._window = Window07408Ea0(client, name + ':window')
        self._pid1_gain = Pid1Gain07408960(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain07408A80(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator07408B40(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock07408D80':
        return self._relock

    @property
    def window(self) -> 'Window07408Ea0':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain07408960':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain07408A80':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator07408B40':
        return self._local_oscillator


class Relock07408D80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window07408Ea0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain07408960:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain07408A80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator07408B40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class StatusParameters07408C60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._baseplate_temperature_limit = DecopReal(client, name + ':baseplate-temperature-limit')
        self._temperature_settle_time = DecopInteger(client, name + ':temperature-settle-time')
        self._pump_lock_settle_time = DecopInteger(client, name + ':pump-lock-settle-time')
        self._settle_down_delay = DecopInteger(client, name + ':settle-down-delay')
        self._power_margin_tolerance_time = DecopInteger(client, name + ':power-margin-tolerance-time')
        self._power_margin_threshold = DecopReal(client, name + ':power-margin-threshold')
        self._cavity_lock_settle_time = DecopInteger(client, name + ':cavity-lock-settle-time')
        self._cavity_lock_tolerance_factor = DecopInteger(client, name + ':cavity-lock-tolerance-factor')
        self._power_lock_settle_time = DecopInteger(client, name + ':power-lock-settle-time')
        self._cavity_scan_duration = DecopInteger(client, name + ':cavity-scan-duration')
        self._power_stabilization_strategy = DecopInteger(client, name + ':power-stabilization-strategy')
        self._power_stabilization_level_low_factor = DecopReal(client, name + ':power-stabilization-level-low-factor')
        self._power_output_relative_error_max = DecopReal(client, name + ':power-output-relative-error-max')
        self._power_output_relative_deviation_max = DecopReal(client, name + ':power-output-relative-deviation-max')
        self._operational_pump_power = DecopReal(client, name + ':operational-pump-power')
        self._degradation_detection_slope_threshold = DecopReal(client, name + ':degradation-detection-slope-threshold')
        self._degradation_detection_measurement_interval = DecopInteger(client, name + ':degradation-detection-measurement-interval')
        self._degradation_detection_number_of_measurements = DecopInteger(client, name + ':degradation-detection-number-of-measurements')

    @property
    def baseplate_temperature_limit(self) -> 'DecopReal':
        return self._baseplate_temperature_limit

    @property
    def temperature_settle_time(self) -> 'DecopInteger':
        return self._temperature_settle_time

    @property
    def pump_lock_settle_time(self) -> 'DecopInteger':
        return self._pump_lock_settle_time

    @property
    def settle_down_delay(self) -> 'DecopInteger':
        return self._settle_down_delay

    @property
    def power_margin_tolerance_time(self) -> 'DecopInteger':
        return self._power_margin_tolerance_time

    @property
    def power_margin_threshold(self) -> 'DecopReal':
        return self._power_margin_threshold

    @property
    def cavity_lock_settle_time(self) -> 'DecopInteger':
        return self._cavity_lock_settle_time

    @property
    def cavity_lock_tolerance_factor(self) -> 'DecopInteger':
        return self._cavity_lock_tolerance_factor

    @property
    def power_lock_settle_time(self) -> 'DecopInteger':
        return self._power_lock_settle_time

    @property
    def cavity_scan_duration(self) -> 'DecopInteger':
        return self._cavity_scan_duration

    @property
    def power_stabilization_strategy(self) -> 'DecopInteger':
        return self._power_stabilization_strategy

    @property
    def power_stabilization_level_low_factor(self) -> 'DecopReal':
        return self._power_stabilization_level_low_factor

    @property
    def power_output_relative_error_max(self) -> 'DecopReal':
        return self._power_output_relative_error_max

    @property
    def power_output_relative_deviation_max(self) -> 'DecopReal':
        return self._power_output_relative_deviation_max

    @property
    def operational_pump_power(self) -> 'DecopReal':
        return self._operational_pump_power

    @property
    def degradation_detection_slope_threshold(self) -> 'DecopReal':
        return self._degradation_detection_slope_threshold

    @property
    def degradation_detection_measurement_interval(self) -> 'DecopInteger':
        return self._degradation_detection_measurement_interval

    @property
    def degradation_detection_number_of_measurements(self) -> 'DecopInteger':
        return self._degradation_detection_number_of_measurements


class PdExt074072E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = MutableDecopReal(client, name + ':cal-offset')
        self._cal_factor = MutableDecopReal(client, name + ':cal-factor')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'MutableDecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'MutableDecopReal':
        return self._cal_factor


class PowerStabilization07407040:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain07407460(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._window = Window07407760(client, name + ':window')
        self._hold_output_on_unlock = MutableDecopBoolean(client, name + ':hold-output-on-unlock')
        self._output_channel = DecopInteger(client, name + ':output-channel')
        self._input_channel_value_act = DecopReal(client, name + ':input-channel-value-act')
        self._state = DecopInteger(client, name + ':state')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain07407460':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def window(self) -> 'Window07407760':
        return self._window

    @property
    def hold_output_on_unlock(self) -> 'MutableDecopBoolean':
        return self._hold_output_on_unlock

    @property
    def output_channel(self) -> 'DecopInteger':
        return self._output_channel

    @property
    def input_channel_value_act(self) -> 'DecopReal':
        return self._input_channel_value_act

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor


class Gain07407460:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d


class Window07407760:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._level_low = MutableDecopReal(client, name + ':level-low')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def level_low(self) -> 'MutableDecopReal':
        return self._level_low

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis


class Config074079A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._source = DecopString(client, name + ':source')
        self._product_name = DecopString(client, name + ':product-name')
        self._date = DecopString(client, name + ':date')
        self._caption = MutableDecopString(client, name + ':caption')
        self._pristine = DecopBoolean(client, name + ':pristine')

    @property
    def source(self) -> 'DecopString':
        return self._source

    @property
    def product_name(self) -> 'DecopString':
        return self._product_name

    @property
    def date(self) -> 'DecopString':
        return self._date

    @property
    def caption(self) -> 'MutableDecopString':
        return self._caption

    @property
    def pristine(self) -> 'DecopBoolean':
        return self._pristine

    def load(self) -> None:
        self.__client.exec(self.__name + ':load', input_stream=None, output_type=None, return_type=None)

    def save(self) -> None:
        self.__client.exec(self.__name + ':save', input_stream=None, output_type=None, return_type=None)

    def import_(self) -> None:
        self.__client.exec(self.__name + ':import', input_stream=None, output_type=None, return_type=None)

    def export(self) -> None:
        self.__client.exec(self.__name + ':export', input_stream=None, output_type=None, return_type=None)

    def retrieve(self) -> None:
        self.__client.exec(self.__name + ':retrieve', input_stream=None, output_type=None, return_type=None)

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)

    def show(self) -> None:
        self.__client.exec(self.__name + ':show', input_stream=None, output_type=None, return_type=None)

    def list(self) -> None:
        self.__client.exec(self.__name + ':list', input_stream=None, output_type=None, return_type=None)


class Laser207407Ac0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = DecopString(client, name + ':type')
        self._product_name = DecopString(client, name + ':product-name')
        self._emission = DecopBoolean(client, name + ':emission')
        self._health = DecopInteger(client, name + ':health')
        self._health_txt = DecopString(client, name + ':health-txt')
        self._dl = Dl07407580(client, name + ':dl')
        self._ctl = Ctl0742C260(client, name + ':ctl')
        self._amp = Amp0742C620(client, name + ':amp')
        self._dpss = Dpss07455860(client, name + ':dpss')
        self._scan = Scan074565E0(client, name + ':scan')
        self._wide_scan = WideScan07455F20(client, name + ':wide-scan')
        self._scope = Scope07455E60(client, name + ':scope')
        self._recorder = Recorder07455Da0(client, name + ':recorder')
        self._nlo = Nlo07456E20(client, name + ':nlo')
        self._uv = Uv06Fc1010(client, name + ':uv')
        self._pd_ext = PdExt07352Bf0(client, name + ':pd-ext')
        self._power_stabilization = PowerStabilization07352D10(client, name + ':power-stabilization')
        self._config = Config07352E90(client, name + ':config')

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def product_name(self) -> 'DecopString':
        return self._product_name

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def health(self) -> 'DecopInteger':
        return self._health

    @property
    def health_txt(self) -> 'DecopString':
        return self._health_txt

    @property
    def dl(self) -> 'Dl07407580':
        return self._dl

    @property
    def ctl(self) -> 'Ctl0742C260':
        return self._ctl

    @property
    def amp(self) -> 'Amp0742C620':
        return self._amp

    @property
    def dpss(self) -> 'Dpss07455860':
        return self._dpss

    @property
    def scan(self) -> 'Scan074565E0':
        return self._scan

    @property
    def wide_scan(self) -> 'WideScan07455F20':
        return self._wide_scan

    @property
    def scope(self) -> 'Scope07455E60':
        return self._scope

    @property
    def recorder(self) -> 'Recorder07455Da0':
        return self._recorder

    @property
    def nlo(self) -> 'Nlo07456E20':
        return self._nlo

    @property
    def uv(self) -> 'Uv06Fc1010':
        return self._uv

    @property
    def pd_ext(self) -> 'PdExt07352Bf0':
        return self._pd_ext

    @property
    def power_stabilization(self) -> 'PowerStabilization07352D10':
        return self._power_stabilization

    @property
    def config(self) -> 'Config07352E90':
        return self._config

    def save(self) -> None:
        self.__client.exec(self.__name + ':save', input_stream=None, output_type=None, return_type=None)

    def load(self) -> None:
        self.__client.exec(self.__name + ':load', input_stream=None, output_type=None, return_type=None)

    def load_head(self) -> None:
        self.__client.exec(self.__name + ':load-head', input_stream=None, output_type=None, return_type=None)


class Dl07407580:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._legacy = DecopBoolean(client, name + ':legacy')
        self._type_ = DecopString(client, name + ':type')
        self._version = DecopString(client, name + ':version')
        self._model = DecopString(client, name + ':model')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._fru_serial_number = DecopString(client, name + ':fru-serial-number')
        self._ontime = DecopInteger(client, name + ':ontime')
        self._ontime_txt = DecopString(client, name + ':ontime-txt')
        self._cc = Cc07407B20(client, name + ':cc')
        self._tc = Tc0742Ce60(client, name + ':tc')
        self._pc = Pc0742Cec0(client, name + ':pc')
        self._lock = Lock0742D4C0(client, name + ':lock')
        self._pressure_compensation = PressureCompensation0742Ba20(client, name + ':pressure-compensation')
        self._pd = Pd0742Bfc0(client, name + ':pd')
        self._factory_settings = FactorySettings0742Bcc0(client, name + ':factory-settings')

    @property
    def legacy(self) -> 'DecopBoolean':
        return self._legacy

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def version(self) -> 'DecopString':
        return self._version

    @property
    def model(self) -> 'DecopString':
        return self._model

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def fru_serial_number(self) -> 'DecopString':
        return self._fru_serial_number

    @property
    def ontime(self) -> 'DecopInteger':
        return self._ontime

    @property
    def ontime_txt(self) -> 'DecopString':
        return self._ontime_txt

    @property
    def cc(self) -> 'Cc07407B20':
        return self._cc

    @property
    def tc(self) -> 'Tc0742Ce60':
        return self._tc

    @property
    def pc(self) -> 'Pc0742Cec0':
        return self._pc

    @property
    def lock(self) -> 'Lock0742D4C0':
        return self._lock

    @property
    def pressure_compensation(self) -> 'PressureCompensation0742Ba20':
        return self._pressure_compensation

    @property
    def pd(self) -> 'Pd0742Bfc0':
        return self._pd

    @property
    def factory_settings(self) -> 'FactorySettings0742Bcc0':
        return self._factory_settings


class Cc07407B20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._variant = DecopString(client, name + ':variant')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._emission = DecopBoolean(client, name + ':emission')
        self._current_set = MutableDecopReal(client, name + ':current-set')
        self._current_offset = MutableDecopReal(client, name + ':current-offset')
        self._current_set_dithering = MutableDecopBoolean(client, name + ':current-set-dithering')
        self._external_input = ExternalInput07407220(client, name + ':external-input')
        self._output_filter = OutputFilter074076A0(client, name + ':output-filter')
        self._current_act = DecopReal(client, name + ':current-act')
        self._positive_polarity = DecopBoolean(client, name + ':positive-polarity')
        self._current_clip = MutableDecopReal(client, name + ':current-clip')
        self._current_clip_limit = DecopReal(client, name + ':current-clip-limit')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._pd = DecopReal(client, name + ':pd')
        self._aux = DecopReal(client, name + ':aux')
        self._snubber = DecopBoolean(client, name + ':snubber')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def variant(self) -> 'DecopString':
        return self._variant

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def current_offset(self) -> 'MutableDecopReal':
        return self._current_offset

    @property
    def current_set_dithering(self) -> 'MutableDecopBoolean':
        return self._current_set_dithering

    @property
    def external_input(self) -> 'ExternalInput07407220':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter074076A0':
        return self._output_filter

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def positive_polarity(self) -> 'DecopBoolean':
        return self._positive_polarity

    @property
    def current_clip(self) -> 'MutableDecopReal':
        return self._current_clip

    @property
    def current_clip_limit(self) -> 'DecopReal':
        return self._current_clip_limit

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def pd(self) -> 'DecopReal':
        return self._pd

    @property
    def aux(self) -> 'DecopReal':
        return self._aux

    @property
    def snubber(self) -> 'DecopBoolean':
        return self._snubber

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput07407220:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter074076A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Tc0742Ce60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput0742D0A0(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop0742D460(client, name + ':t-loop')
        self._limits = Limits0742D220(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput0742D0A0':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop0742D460':
        return self._t_loop

    @property
    def limits(self) -> 'Limits0742D220':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput0742D0A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop0742D460:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits0742D220:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc0742Cec0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput0742D280(client, name + ':external-input')
        self._output_filter = OutputFilter0742D100(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput0742D280':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter0742D100':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput0742D280:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter0742D100:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Lock0742D4C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = MutableDecopInteger(client, name + ':type')
        self._lock_without_lockpoint = MutableDecopBoolean(client, name + ':lock-without-lockpoint')
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._spectrum_input_channel = MutableDecopInteger(client, name + ':spectrum-input-channel')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock0742D2E0(client, name + ':relock')
        self._reset = Reset0742Be40(client, name + ':reset')
        self._window = Window0742Ba80(client, name + ':window')
        self._pid1 = Pid10742B780(client, name + ':pid1')
        self._pid2 = Pid20742Bd20(client, name + ':pid2')
        self._lockin = Lockin0742Bae0(client, name + ':lockin')
        self._lockpoint = Lockpoint0742Bd80(client, name + ':lockpoint')
        self._candidate_filter = CandidateFilter0742B960(client, name + ':candidate-filter')
        self._candidates = DecopBinary(client, name + ':candidates')
        self._locking_delay = MutableDecopInteger(client, name + ':locking-delay')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def type_(self) -> 'MutableDecopInteger':
        return self._type_

    @property
    def lock_without_lockpoint(self) -> 'MutableDecopBoolean':
        return self._lock_without_lockpoint

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def spectrum_input_channel(self) -> 'MutableDecopInteger':
        return self._spectrum_input_channel

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock0742D2E0':
        return self._relock

    @property
    def reset(self) -> 'Reset0742Be40':
        return self._reset

    @property
    def window(self) -> 'Window0742Ba80':
        return self._window

    @property
    def pid1(self) -> 'Pid10742B780':
        return self._pid1

    @property
    def pid2(self) -> 'Pid20742Bd20':
        return self._pid2

    @property
    def lockin(self) -> 'Lockin0742Bae0':
        return self._lockin

    @property
    def lockpoint(self) -> 'Lockpoint0742Bd80':
        return self._lockpoint

    @property
    def candidate_filter(self) -> 'CandidateFilter0742B960':
        return self._candidate_filter

    @property
    def candidates(self) -> 'DecopBinary':
        return self._candidates

    @property
    def locking_delay(self) -> 'MutableDecopInteger':
        return self._locking_delay

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace

    def show_candidates(self) -> None:
        self.__client.exec(self.__name + ':show-candidates', input_stream=None, output_type=None, return_type=None)

    def find_candidates(self) -> None:
        self.__client.exec(self.__name + ':find-candidates', input_stream=None, output_type=None, return_type=None)

    def select_lockpoint(self) -> None:
        self.__client.exec(self.__name + ':select-lockpoint', input_stream=None, output_type=None, return_type=None)

    def close(self) -> None:
        self.__client.exec(self.__name + ':close', input_stream=None, output_type=None, return_type=None)

    def open(self) -> None:
        self.__client.exec(self.__name + ':open', input_stream=None, output_type=None, return_type=None)


class Relock0742D2E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Reset0742Be40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Window0742Ba80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._level_high = MutableDecopReal(client, name + ':level-high')
        self._level_low = MutableDecopReal(client, name + ':level-low')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def level_high(self) -> 'MutableDecopReal':
        return self._level_high

    @property
    def level_low(self) -> 'MutableDecopReal':
        return self._level_low

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis


class Pid10742B780:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain0742B600(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._slope = MutableDecopBoolean(client, name + ':slope')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._outputlimit = Outputlimit0742Bc00(client, name + ':outputlimit')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._lock_state = DecopBoolean(client, name + ':lock-state')
        self._hold_state = DecopBoolean(client, name + ':hold-state')
        self._regulating_state = DecopBoolean(client, name + ':regulating-state')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain0742B600':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def slope(self) -> 'MutableDecopBoolean':
        return self._slope

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def outputlimit(self) -> 'Outputlimit0742Bc00':
        return self._outputlimit

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def lock_state(self) -> 'DecopBoolean':
        return self._lock_state

    @property
    def hold_state(self) -> 'DecopBoolean':
        return self._hold_state

    @property
    def regulating_state(self) -> 'DecopBoolean':
        return self._regulating_state


class Gain0742B600:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')
        self._fc_ip = DecopReal(client, name + ':fc-ip')
        self._fc_pd = DecopReal(client, name + ':fc-pd')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled

    @property
    def fc_ip(self) -> 'DecopReal':
        return self._fc_ip

    @property
    def fc_pd(self) -> 'DecopReal':
        return self._fc_pd


class Outputlimit0742Bc00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._max = MutableDecopReal(client, name + ':max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def max(self) -> 'MutableDecopReal':
        return self._max


class Pid20742Bd20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain0742B840(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._slope = MutableDecopBoolean(client, name + ':slope')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._outputlimit = Outputlimit0742C080(client, name + ':outputlimit')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._lock_state = DecopBoolean(client, name + ':lock-state')
        self._hold_state = DecopBoolean(client, name + ':hold-state')
        self._regulating_state = DecopBoolean(client, name + ':regulating-state')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain0742B840':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def slope(self) -> 'MutableDecopBoolean':
        return self._slope

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def outputlimit(self) -> 'Outputlimit0742C080':
        return self._outputlimit

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def lock_state(self) -> 'DecopBoolean':
        return self._lock_state

    @property
    def hold_state(self) -> 'DecopBoolean':
        return self._hold_state

    @property
    def regulating_state(self) -> 'DecopBoolean':
        return self._regulating_state


class Gain0742B840:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')
        self._fc_ip = DecopReal(client, name + ':fc-ip')
        self._fc_pd = DecopReal(client, name + ':fc-pd')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled

    @property
    def fc_ip(self) -> 'DecopReal':
        return self._fc_ip

    @property
    def fc_pd(self) -> 'DecopReal':
        return self._fc_pd


class Outputlimit0742C080:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._max = MutableDecopReal(client, name + ':max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def max(self) -> 'MutableDecopReal':
        return self._max


class Lockin0742Bae0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._modulation_enabled = MutableDecopBoolean(client, name + ':modulation-enabled')
        self._modulation_output_channel = MutableDecopInteger(client, name + ':modulation-output-channel')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')
        self._lock_level = MutableDecopReal(client, name + ':lock-level')
        self._auto_lir = AutoLir0742C140(client, name + ':auto-lir')

    @property
    def modulation_enabled(self) -> 'MutableDecopBoolean':
        return self._modulation_enabled

    @property
    def modulation_output_channel(self) -> 'MutableDecopInteger':
        return self._modulation_output_channel

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    @property
    def lock_level(self) -> 'MutableDecopReal':
        return self._lock_level

    @property
    def auto_lir(self) -> 'AutoLir0742C140':
        return self._auto_lir


class AutoLir0742C140:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._progress = DecopInteger(client, name + ':progress')

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    def auto_lir(self) -> None:
        self.__client.exec(self.__name + ':auto-lir', input_stream=None, output_type=None, return_type=None)


class Lockpoint0742Bd80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._type_ = DecopString(client, name + ':type')

    @property
    def type_(self) -> 'DecopString':
        return self._type_


class CandidateFilter0742B960:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._top = MutableDecopBoolean(client, name + ':top')
        self._bottom = MutableDecopBoolean(client, name + ':bottom')
        self._positive_edge = MutableDecopBoolean(client, name + ':positive-edge')
        self._negative_edge = MutableDecopBoolean(client, name + ':negative-edge')
        self._edge_level = MutableDecopReal(client, name + ':edge-level')
        self._peak_noise_tolerance = MutableDecopReal(client, name + ':peak-noise-tolerance')
        self._edge_min_distance = MutableDecopInteger(client, name + ':edge-min-distance')

    @property
    def top(self) -> 'MutableDecopBoolean':
        return self._top

    @property
    def bottom(self) -> 'MutableDecopBoolean':
        return self._bottom

    @property
    def positive_edge(self) -> 'MutableDecopBoolean':
        return self._positive_edge

    @property
    def negative_edge(self) -> 'MutableDecopBoolean':
        return self._negative_edge

    @property
    def edge_level(self) -> 'MutableDecopReal':
        return self._edge_level

    @property
    def peak_noise_tolerance(self) -> 'MutableDecopReal':
        return self._peak_noise_tolerance

    @property
    def edge_min_distance(self) -> 'MutableDecopInteger':
        return self._edge_min_distance


class PressureCompensation0742Ba20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._air_pressure = DecopReal(client, name + ':air-pressure')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._compensation_voltage = DecopReal(client, name + ':compensation-voltage')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def air_pressure(self) -> 'DecopReal':
        return self._air_pressure

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def compensation_voltage(self) -> 'DecopReal':
        return self._compensation_voltage


class Pd0742Bfc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class FactorySettings0742Bcc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._threshold_current = DecopReal(client, name + ':threshold-current')
        self._power = DecopReal(client, name + ':power')
        self._cc = Cc0742Bde0(client, name + ':cc')
        self._tc = Tc0742C8C0(client, name + ':tc')
        self._pc = Pc0742C200(client, name + ':pc')
        self._pd = Pd0742C500(client, name + ':pd')

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def threshold_current(self) -> 'DecopReal':
        return self._threshold_current

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cc(self) -> 'Cc0742Bde0':
        return self._cc

    @property
    def tc(self) -> 'Tc0742C8C0':
        return self._tc

    @property
    def pc(self) -> 'Pc0742C200':
        return self._pc

    @property
    def pd(self) -> 'Pd0742C500':
        return self._pd

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Cc0742Bde0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_clip = DecopReal(client, name + ':current-clip')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._positive_polarity = DecopBoolean(client, name + ':positive-polarity')
        self._snubber = DecopBoolean(client, name + ':snubber')

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_clip(self) -> 'DecopReal':
        return self._current_clip

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def positive_polarity(self) -> 'DecopBoolean':
        return self._positive_polarity

    @property
    def snubber(self) -> 'DecopBoolean':
        return self._snubber


class Tc0742C8C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')
        self._ntc_parallel_resistance = DecopReal(client, name + ':ntc-parallel-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance

    @property
    def ntc_parallel_resistance(self) -> 'DecopReal':
        return self._ntc_parallel_resistance


class Pc0742C200:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._slew_rate = DecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = DecopBoolean(client, name + ':slew-rate-enabled')
        self._pressure_compensation_factor = DecopReal(client, name + ':pressure-compensation-factor')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def slew_rate(self) -> 'DecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'DecopBoolean':
        return self._slew_rate_enabled

    @property
    def pressure_compensation_factor(self) -> 'DecopReal':
        return self._pressure_compensation_factor


class Pd0742C500:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Ctl0742C260:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._fpga_fw_ver = DecopInteger(client, name + ':fpga-fw-ver')
        self._wavelength_set = MutableDecopReal(client, name + ':wavelength-set')
        self._wavelength_act = DecopReal(client, name + ':wavelength-act')
        self._wavelength_min = DecopReal(client, name + ':wavelength-min')
        self._wavelength_max = DecopReal(client, name + ':wavelength-max')
        self._tuning_current_min = DecopReal(client, name + ':tuning-current-min')
        self._tuning_power_min = DecopReal(client, name + ':tuning-power-min')
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._head_temperature = DecopReal(client, name + ':head-temperature')
        self._optimization = Optimization0742Cbc0(client, name + ':optimization')
        self._remote_control = RemoteControl0742C320(client, name + ':remote-control')
        self._mode_control = ModeControl0742C380(client, name + ':mode-control')
        self._motor = Motor0742C920(client, name + ':motor')
        self._power = Power0742C440(client, name + ':power')
        self._factory_settings = FactorySettings0742C5C0(client, name + ':factory-settings')

    @property
    def fpga_fw_ver(self) -> 'DecopInteger':
        return self._fpga_fw_ver

    @property
    def wavelength_set(self) -> 'MutableDecopReal':
        return self._wavelength_set

    @property
    def wavelength_act(self) -> 'DecopReal':
        return self._wavelength_act

    @property
    def wavelength_min(self) -> 'DecopReal':
        return self._wavelength_min

    @property
    def wavelength_max(self) -> 'DecopReal':
        return self._wavelength_max

    @property
    def tuning_current_min(self) -> 'DecopReal':
        return self._tuning_current_min

    @property
    def tuning_power_min(self) -> 'DecopReal':
        return self._tuning_power_min

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def head_temperature(self) -> 'DecopReal':
        return self._head_temperature

    @property
    def optimization(self) -> 'Optimization0742Cbc0':
        return self._optimization

    @property
    def remote_control(self) -> 'RemoteControl0742C320':
        return self._remote_control

    @property
    def mode_control(self) -> 'ModeControl0742C380':
        return self._mode_control

    @property
    def motor(self) -> 'Motor0742C920':
        return self._motor

    @property
    def power(self) -> 'Power0742C440':
        return self._power

    @property
    def factory_settings(self) -> 'FactorySettings0742C5C0':
        return self._factory_settings


class Optimization0742Cbc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._progress = DecopInteger(client, name + ':progress')

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    def smile(self) -> None:
        self.__client.exec(self.__name + ':smile', input_stream=None, output_type=None, return_type=None)

    def flow(self) -> None:
        self.__client.exec(self.__name + ':flow', input_stream=None, output_type=None, return_type=None)

    def abort(self) -> None:
        self.__client.exec(self.__name + ':abort', input_stream=None, output_type=None, return_type=None)


class RemoteControl0742C320:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class ModeControl0742C380:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._loop_enabled = MutableDecopBoolean(client, name + ':loop-enabled')

    @property
    def loop_enabled(self) -> 'MutableDecopBoolean':
        return self._loop_enabled


class Motor0742C920:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._position_accuracy_fullstep = DecopInteger(client, name + ':position-accuracy-fullstep')
        self._position_hysteresis_fullstep = DecopInteger(client, name + ':position-hysteresis-fullstep')
        self._position_accuracy_microstep = DecopInteger(client, name + ':position-accuracy-microstep')
        self._position_hysteresis_microstep = DecopInteger(client, name + ':position-hysteresis-microstep')
        self._microsteps = MutableDecopBoolean(client, name + ':microsteps')
        self._power_save_disabled = DecopBoolean(client, name + ':power-save-disabled')

    @property
    def position_accuracy_fullstep(self) -> 'DecopInteger':
        return self._position_accuracy_fullstep

    @property
    def position_hysteresis_fullstep(self) -> 'DecopInteger':
        return self._position_hysteresis_fullstep

    @property
    def position_accuracy_microstep(self) -> 'DecopInteger':
        return self._position_accuracy_microstep

    @property
    def position_hysteresis_microstep(self) -> 'DecopInteger':
        return self._position_hysteresis_microstep

    @property
    def microsteps(self) -> 'MutableDecopBoolean':
        return self._microsteps

    @property
    def power_save_disabled(self) -> 'DecopBoolean':
        return self._power_save_disabled


class Power0742C440:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_act = DecopReal(client, name + ':power-act')

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act


class FactorySettings0742C5C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength_min = DecopReal(client, name + ':wavelength-min')
        self._wavelength_max = DecopReal(client, name + ':wavelength-max')
        self._tuning_current_min = DecopReal(client, name + ':tuning-current-min')
        self._tuning_power_min = DecopReal(client, name + ':tuning-power-min')

    @property
    def wavelength_min(self) -> 'DecopReal':
        return self._wavelength_min

    @property
    def wavelength_max(self) -> 'DecopReal':
        return self._wavelength_max

    @property
    def tuning_current_min(self) -> 'DecopReal':
        return self._tuning_current_min

    @property
    def tuning_power_min(self) -> 'DecopReal':
        return self._tuning_power_min

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Amp0742C620:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._legacy = DecopBoolean(client, name + ':legacy')
        self._type_ = DecopString(client, name + ':type')
        self._version = DecopString(client, name + ':version')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._fru_serial_number = DecopString(client, name + ':fru-serial-number')
        self._ontime = DecopInteger(client, name + ':ontime')
        self._ontime_txt = DecopString(client, name + ':ontime-txt')
        self._cc = Cc0742C680(client, name + ':cc')
        self._tc = Tc0742Caa0(client, name + ':tc')
        self._pd = Pd074559E0(client, name + ':pd')
        self._seed_limits = SeedLimits074555C0(client, name + ':seed-limits')
        self._output_limits = OutputLimits07455380(client, name + ':output-limits')
        self._seedonly_check = SeedonlyCheck074552C0(client, name + ':seedonly-check')
        self._factory_settings = FactorySettings07455080(client, name + ':factory-settings')

    @property
    def legacy(self) -> 'DecopBoolean':
        return self._legacy

    @property
    def type_(self) -> 'DecopString':
        return self._type_

    @property
    def version(self) -> 'DecopString':
        return self._version

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def fru_serial_number(self) -> 'DecopString':
        return self._fru_serial_number

    @property
    def ontime(self) -> 'DecopInteger':
        return self._ontime

    @property
    def ontime_txt(self) -> 'DecopString':
        return self._ontime_txt

    @property
    def cc(self) -> 'Cc0742C680':
        return self._cc

    @property
    def tc(self) -> 'Tc0742Caa0':
        return self._tc

    @property
    def pd(self) -> 'Pd074559E0':
        return self._pd

    @property
    def seed_limits(self) -> 'SeedLimits074555C0':
        return self._seed_limits

    @property
    def output_limits(self) -> 'OutputLimits07455380':
        return self._output_limits

    @property
    def seedonly_check(self) -> 'SeedonlyCheck074552C0':
        return self._seedonly_check

    @property
    def factory_settings(self) -> 'FactorySettings07455080':
        return self._factory_settings


class Cc0742C680:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._variant = DecopString(client, name + ':variant')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._emission = DecopBoolean(client, name + ':emission')
        self._current_set = MutableDecopReal(client, name + ':current-set')
        self._current_offset = MutableDecopReal(client, name + ':current-offset')
        self._output_filter = OutputFilter0742Ca40(client, name + ':output-filter')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_clip = MutableDecopReal(client, name + ':current-clip')
        self._current_clip_limit = DecopReal(client, name + ':current-clip-limit')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._voltage_out = DecopReal(client, name + ':voltage-out')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._aux = DecopReal(client, name + ':aux')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def variant(self) -> 'DecopString':
        return self._variant

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def current_set(self) -> 'MutableDecopReal':
        return self._current_set

    @property
    def current_offset(self) -> 'MutableDecopReal':
        return self._current_offset

    @property
    def output_filter(self) -> 'OutputFilter0742Ca40':
        return self._output_filter

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_clip(self) -> 'MutableDecopReal':
        return self._current_clip

    @property
    def current_clip_limit(self) -> 'DecopReal':
        return self._current_clip_limit

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def voltage_out(self) -> 'DecopReal':
        return self._voltage_out

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def aux(self) -> 'DecopReal':
        return self._aux

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class OutputFilter0742Ca40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Tc0742Caa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput0742Cb60(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop07455020(client, name + ':t-loop')
        self._limits = Limits074556E0(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput0742Cb60':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop07455020':
        return self._t_loop

    @property
    def limits(self) -> 'Limits074556E0':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput0742Cb60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop07455020:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits074556E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pd074559E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._seed = Seed074550E0(client, name + ':seed')
        self._amp = Amp07454E40(client, name + ':amp')

    @property
    def seed(self) -> 'Seed074550E0':
        return self._seed

    @property
    def amp(self) -> 'Amp07454E40':
        return self._amp


class Seed074550E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp07454E40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class SeedLimits074555C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class OutputLimits07455380:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class SeedonlyCheck074552C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._warning_delay = DecopReal(client, name + ':warning-delay')
        self._shutdown_delay = DecopReal(client, name + ':shutdown-delay')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def warning_delay(self) -> 'DecopReal':
        return self._warning_delay

    @property
    def shutdown_delay(self) -> 'DecopReal':
        return self._shutdown_delay

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class FactorySettings07455080:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._power = DecopReal(client, name + ':power')
        self._cc = Cc07455320(client, name + ':cc')
        self._tc = Tc07455140(client, name + ':tc')
        self._pd = Pd07455620(client, name + ':pd')
        self._seed_limits = SeedLimits07454F00(client, name + ':seed-limits')
        self._output_limits = OutputLimits07454Fc0(client, name + ':output-limits')
        self._seedonly_check = SeedonlyCheck074551A0(client, name + ':seedonly-check')

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cc(self) -> 'Cc07455320':
        return self._cc

    @property
    def tc(self) -> 'Tc07455140':
        return self._tc

    @property
    def pd(self) -> 'Pd07455620':
        return self._pd

    @property
    def seed_limits(self) -> 'SeedLimits07454F00':
        return self._seed_limits

    @property
    def output_limits(self) -> 'OutputLimits07454Fc0':
        return self._output_limits

    @property
    def seedonly_check(self) -> 'SeedonlyCheck074551A0':
        return self._seedonly_check

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Cc07455320:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_clip = DecopReal(client, name + ':current-clip')
        self._voltage_clip = DecopReal(client, name + ':voltage-clip')

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_clip(self) -> 'DecopReal':
        return self._current_clip

    @property
    def voltage_clip(self) -> 'DecopReal':
        return self._voltage_clip


class Tc07455140:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')
        self._ntc_parallel_resistance = DecopReal(client, name + ':ntc-parallel-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance

    @property
    def ntc_parallel_resistance(self) -> 'DecopReal':
        return self._ntc_parallel_resistance


class Pd07455620:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._seed = Seed07455680(client, name + ':seed')
        self._amp = Amp074557A0(client, name + ':amp')

    @property
    def seed(self) -> 'Seed07455680':
        return self._seed

    @property
    def amp(self) -> 'Amp074557A0':
        return self._amp


class Seed07455680:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp074557A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class SeedLimits07454F00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay


class OutputLimits07454Fc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_min_warning_delay = DecopReal(client, name + ':power-min-warning-delay')
        self._power_min_shutdown_delay = DecopReal(client, name + ':power-min-shutdown-delay')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_max_warning_delay = DecopReal(client, name + ':power-max-warning-delay')
        self._power_max_shutdown_delay = DecopReal(client, name + ':power-max-shutdown-delay')

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_min_warning_delay(self) -> 'DecopReal':
        return self._power_min_warning_delay

    @property
    def power_min_shutdown_delay(self) -> 'DecopReal':
        return self._power_min_shutdown_delay

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_max_warning_delay(self) -> 'DecopReal':
        return self._power_max_warning_delay

    @property
    def power_max_shutdown_delay(self) -> 'DecopReal':
        return self._power_max_shutdown_delay


class SeedonlyCheck074551A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._warning_delay = DecopReal(client, name + ':warning-delay')
        self._shutdown_delay = DecopReal(client, name + ':shutdown-delay')

    @property
    def warning_delay(self) -> 'DecopReal':
        return self._warning_delay

    @property
    def shutdown_delay(self) -> 'DecopReal':
        return self._shutdown_delay


class Dpss07455860:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._tc_status = DecopInteger(client, name + ':tc-status')
        self._tc_status_txt = DecopString(client, name + ':tc-status-txt')
        self._error_code = DecopInteger(client, name + ':error-code')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._power_set = MutableDecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_max = DecopReal(client, name + ':current-max')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def tc_status(self) -> 'DecopInteger':
        return self._tc_status

    @property
    def tc_status_txt(self) -> 'DecopString':
        return self._tc_status_txt

    @property
    def error_code(self) -> 'DecopInteger':
        return self._error_code

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def power_set(self) -> 'MutableDecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max


class Scan074565E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._hold = MutableDecopBoolean(client, name + ':hold')
        self._signal_type = MutableDecopInteger(client, name + ':signal-type')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._unit = DecopString(client, name + ':unit')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')
        self._start = MutableDecopReal(client, name + ':start')
        self._end = MutableDecopReal(client, name + ':end')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def hold(self) -> 'MutableDecopBoolean':
        return self._hold

    @property
    def signal_type(self) -> 'MutableDecopInteger':
        return self._signal_type

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset

    @property
    def start(self) -> 'MutableDecopReal':
        return self._start

    @property
    def end(self) -> 'MutableDecopReal':
        return self._end


class WideScan07455F20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._scan_begin = MutableDecopReal(client, name + ':scan-begin')
        self._scan_end = MutableDecopReal(client, name + ':scan-end')
        self._continuous_mode = MutableDecopBoolean(client, name + ':continuous-mode')
        self._shape = MutableDecopInteger(client, name + ':shape')
        self._offset = MutableDecopReal(client, name + ':offset')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._speed = MutableDecopReal(client, name + ':speed')
        self._speed_min = DecopReal(client, name + ':speed-min')
        self._speed_max = DecopReal(client, name + ':speed-max')
        self._duration = MutableDecopReal(client, name + ':duration')
        self._value_set = MutableDecopReal(client, name + ':value-set')
        self._value_act = DecopReal(client, name + ':value-act')
        self._value_unit = DecopString(client, name + ':value-unit')
        self._recorder_stepsize_set = MutableDecopReal(client, name + ':recorder-stepsize-set')
        self._recorder_stepsize = DecopReal(client, name + ':recorder-stepsize')
        self._progress = DecopInteger(client, name + ':progress')
        self._remaining_time = DecopInteger(client, name + ':remaining-time')
        self._trigger = Trigger07455C20(client, name + ':trigger')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def scan_begin(self) -> 'MutableDecopReal':
        return self._scan_begin

    @property
    def scan_end(self) -> 'MutableDecopReal':
        return self._scan_end

    @property
    def continuous_mode(self) -> 'MutableDecopBoolean':
        return self._continuous_mode

    @property
    def shape(self) -> 'MutableDecopInteger':
        return self._shape

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def speed(self) -> 'MutableDecopReal':
        return self._speed

    @property
    def speed_min(self) -> 'DecopReal':
        return self._speed_min

    @property
    def speed_max(self) -> 'DecopReal':
        return self._speed_max

    @property
    def duration(self) -> 'MutableDecopReal':
        return self._duration

    @property
    def value_set(self) -> 'MutableDecopReal':
        return self._value_set

    @property
    def value_act(self) -> 'DecopReal':
        return self._value_act

    @property
    def value_unit(self) -> 'DecopString':
        return self._value_unit

    @property
    def recorder_stepsize_set(self) -> 'MutableDecopReal':
        return self._recorder_stepsize_set

    @property
    def recorder_stepsize(self) -> 'DecopReal':
        return self._recorder_stepsize

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def remaining_time(self) -> 'DecopInteger':
        return self._remaining_time

    @property
    def trigger(self) -> 'Trigger07455C20':
        return self._trigger

    def start(self) -> None:
        self.__client.exec(self.__name + ':start', input_stream=None, output_type=None, return_type=None)

    def stop(self) -> None:
        self.__client.exec(self.__name + ':stop', input_stream=None, output_type=None, return_type=None)

    def set_output_to_zoom_offset(self) -> None:
        self.__client.exec(self.__name + ':set-output-to-zoom-offset', input_stream=None, output_type=None, return_type=None)

    def set_scan_range_to_zoom_range(self) -> None:
        self.__client.exec(self.__name + ':set-scan-range-to-zoom-range', input_stream=None, output_type=None, return_type=None)

    def set_zoom_range_to_scan_range(self) -> None:
        self.__client.exec(self.__name + ':set-zoom-range-to-scan-range', input_stream=None, output_type=None, return_type=None)


class Trigger07455C20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_enabled = MutableDecopBoolean(client, name + ':input-enabled')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._output_enabled = MutableDecopBoolean(client, name + ':output-enabled')
        self._output_channel = MutableDecopInteger(client, name + ':output-channel')
        self._output_threshold = MutableDecopReal(client, name + ':output-threshold')

    @property
    def input_enabled(self) -> 'MutableDecopBoolean':
        return self._input_enabled

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def output_enabled(self) -> 'MutableDecopBoolean':
        return self._output_enabled

    @property
    def output_channel(self) -> 'MutableDecopInteger':
        return self._output_channel

    @property
    def output_threshold(self) -> 'MutableDecopReal':
        return self._output_threshold


class Scope07455E60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel107455B60(client, name + ':channel1')
        self._channel2 = Channel207456160(client, name + ':channel2')
        self._channelx = Channelx07456580(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel107455B60':
        return self._channel1

    @property
    def channel2(self) -> 'Channel207456160':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx07456580':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel107455B60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel207456160:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx07456580:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Recorder07455Da0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._inputs = Inputs07455Aa0(client, name + ':inputs')
        self._recording_mode = MutableDecopInteger(client, name + ':recording-mode')
        self._recording_time = MutableDecopReal(client, name + ':recording-time')
        self._sample_count_set = MutableDecopInteger(client, name + ':sample-count-set')
        self._sample_count = DecopInteger(client, name + ':sample-count')
        self._sampling_interval = DecopReal(client, name + ':sampling-interval')
        self._sampling_rate = DecopReal(client, name + ':sampling-rate')
        self._memory_size = DecopInteger(client, name + ':memory-size')
        self._data = Data07456Fa0(client, name + ':data')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def inputs(self) -> 'Inputs07455Aa0':
        return self._inputs

    @property
    def recording_mode(self) -> 'MutableDecopInteger':
        return self._recording_mode

    @property
    def recording_time(self) -> 'MutableDecopReal':
        return self._recording_time

    @property
    def sample_count_set(self) -> 'MutableDecopInteger':
        return self._sample_count_set

    @property
    def sample_count(self) -> 'DecopInteger':
        return self._sample_count

    @property
    def sampling_interval(self) -> 'DecopReal':
        return self._sampling_interval

    @property
    def sampling_rate(self) -> 'DecopReal':
        return self._sampling_rate

    @property
    def memory_size(self) -> 'DecopInteger':
        return self._memory_size

    @property
    def data(self) -> 'Data07456Fa0':
        return self._data


class Inputs07455Aa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._channel1 = Channel107456280(client, name + ':channel1')
        self._channel2 = Channel207456040(client, name + ':channel2')
        self._channelx = Channelx07456400(client, name + ':channelx')

    @property
    def channel1(self) -> 'Channel107456280':
        return self._channel1

    @property
    def channel2(self) -> 'Channel207456040':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx07456400':
        return self._channelx


class Channel107456280:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._low_pass_filter = LowPassFilter07455Fe0(client, name + ':low-pass-filter')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def low_pass_filter(self) -> 'LowPassFilter07455Fe0':
        return self._low_pass_filter


class LowPassFilter07455Fe0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._cut_off_frequency = MutableDecopReal(client, name + ':cut-off-frequency')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def cut_off_frequency(self) -> 'MutableDecopReal':
        return self._cut_off_frequency


class Channel207456040:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._low_pass_filter = LowPassFilter074563A0(client, name + ':low-pass-filter')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def low_pass_filter(self) -> 'LowPassFilter074563A0':
        return self._low_pass_filter


class LowPassFilter074563A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._cut_off_frequency = MutableDecopReal(client, name + ':cut-off-frequency')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def cut_off_frequency(self) -> 'MutableDecopReal':
        return self._cut_off_frequency


class Channelx07456400:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal


class Data07456Fa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._channel1 = Channel107456A60(client, name + ':channel1')
        self._channel2 = Channel207456Dc0(client, name + ':channel2')
        self._channelx = Channelx07456D00(client, name + ':channelx')
        self._zoom_data = DecopBinary(client, name + ':zoom-data')
        self._zoom_offset = MutableDecopReal(client, name + ':zoom-offset')
        self._zoom_amplitude = MutableDecopReal(client, name + ':zoom-amplitude')
        self._recorded_sampling_interval = DecopReal(client, name + ':recorded-sampling-interval')
        self._recorded_sample_count = DecopInteger(client, name + ':recorded-sample-count')
        self._last_recorded_sample = DecopInteger(client, name + ':last-recorded-sample')
        self._last_valid_sample = DecopInteger(client, name + ':last-valid-sample')

    @property
    def channel1(self) -> 'Channel107456A60':
        return self._channel1

    @property
    def channel2(self) -> 'Channel207456Dc0':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx07456D00':
        return self._channelx

    @property
    def zoom_data(self) -> 'DecopBinary':
        return self._zoom_data

    @property
    def zoom_offset(self) -> 'MutableDecopReal':
        return self._zoom_offset

    @property
    def zoom_amplitude(self) -> 'MutableDecopReal':
        return self._zoom_amplitude

    @property
    def recorded_sampling_interval(self) -> 'DecopReal':
        return self._recorded_sampling_interval

    @property
    def recorded_sample_count(self) -> 'DecopInteger':
        return self._recorded_sample_count

    @property
    def last_recorded_sample(self) -> 'DecopInteger':
        return self._last_recorded_sample

    @property
    def last_valid_sample(self) -> 'DecopInteger':
        return self._last_valid_sample

    def zoom_out(self) -> None:
        self.__client.exec(self.__name + ':zoom-out', input_stream=None, output_type=None, return_type=None)

    def get_data(self) -> None:
        self.__client.exec(self.__name + ':get-data', input_stream=None, output_type=None, return_type=None)

    def show_data(self) -> None:
        self.__client.exec(self.__name + ':show-data', input_stream=None, output_type=None, return_type=None)


class Channel107456A60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel207456Dc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx07456D00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Nlo07456E20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._servo = Servo07456Ac0(client, name + ':servo')
        self._pd = Pd07453F40(client, name + ':pd')
        self._power_optimization = PowerOptimization074542A0(client, name + ':power-optimization')
        self._auto_nlo = AutoNlo07454D20(client, name + ':auto-nlo')
        self._shg = Shg074548A0(client, name + ':shg')
        self._fhg = Fhg06Fbf870(client, name + ':fhg')
        self._ssw_ver = DecopString(client, name + ':ssw-ver')

    @property
    def servo(self) -> 'Servo07456Ac0':
        return self._servo

    @property
    def pd(self) -> 'Pd07453F40':
        return self._pd

    @property
    def power_optimization(self) -> 'PowerOptimization074542A0':
        return self._power_optimization

    @property
    def auto_nlo(self) -> 'AutoNlo07454D20':
        return self._auto_nlo

    @property
    def shg(self) -> 'Shg074548A0':
        return self._shg

    @property
    def fhg(self) -> 'Fhg06Fbf870':
        return self._fhg

    @property
    def ssw_ver(self) -> 'DecopString':
        return self._ssw_ver


class Servo07456Ac0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ta1_hor = Ta1Hor07456E80(client, name + ':ta1-hor')
        self._ta1_vert = Ta1Vert07456Ee0(client, name + ':ta1-vert')
        self._ta2_hor = Ta2Hor074567C0(client, name + ':ta2-hor')
        self._ta2_vert = Ta2Vert074566A0(client, name + ':ta2-vert')
        self._shg1_hor = Shg1Hor07457120(client, name + ':shg1-hor')
        self._shg1_vert = Shg1Vert074571E0(client, name + ':shg1-vert')
        self._shg2_hor = Shg2Hor07456640(client, name + ':shg2-hor')
        self._shg2_vert = Shg2Vert07456880(client, name + ':shg2-vert')
        self._fhg1_hor = Fhg1Hor07456940(client, name + ':fhg1-hor')
        self._fhg1_vert = Fhg1Vert07456Be0(client, name + ':fhg1-vert')
        self._fhg2_hor = Fhg2Hor07457420(client, name + ':fhg2-hor')
        self._fhg2_vert = Fhg2Vert074575A0(client, name + ':fhg2-vert')
        self._fiber1_hor = Fiber1Hor074572A0(client, name + ':fiber1-hor')
        self._fiber1_vert = Fiber1Vert07457300(client, name + ':fiber1-vert')
        self._fiber2_hor = Fiber2Hor074573C0(client, name + ':fiber2-hor')
        self._fiber2_vert = Fiber2Vert07453D00(client, name + ':fiber2-vert')
        self._uv_outcpl = UvOutcpl07454000(client, name + ':uv-outcpl')
        self._uv_cryst = UvCryst07453Fa0(client, name + ':uv-cryst')

    @property
    def ta1_hor(self) -> 'Ta1Hor07456E80':
        return self._ta1_hor

    @property
    def ta1_vert(self) -> 'Ta1Vert07456Ee0':
        return self._ta1_vert

    @property
    def ta2_hor(self) -> 'Ta2Hor074567C0':
        return self._ta2_hor

    @property
    def ta2_vert(self) -> 'Ta2Vert074566A0':
        return self._ta2_vert

    @property
    def shg1_hor(self) -> 'Shg1Hor07457120':
        return self._shg1_hor

    @property
    def shg1_vert(self) -> 'Shg1Vert074571E0':
        return self._shg1_vert

    @property
    def shg2_hor(self) -> 'Shg2Hor07456640':
        return self._shg2_hor

    @property
    def shg2_vert(self) -> 'Shg2Vert07456880':
        return self._shg2_vert

    @property
    def fhg1_hor(self) -> 'Fhg1Hor07456940':
        return self._fhg1_hor

    @property
    def fhg1_vert(self) -> 'Fhg1Vert07456Be0':
        return self._fhg1_vert

    @property
    def fhg2_hor(self) -> 'Fhg2Hor07457420':
        return self._fhg2_hor

    @property
    def fhg2_vert(self) -> 'Fhg2Vert074575A0':
        return self._fhg2_vert

    @property
    def fiber1_hor(self) -> 'Fiber1Hor074572A0':
        return self._fiber1_hor

    @property
    def fiber1_vert(self) -> 'Fiber1Vert07457300':
        return self._fiber1_vert

    @property
    def fiber2_hor(self) -> 'Fiber2Hor074573C0':
        return self._fiber2_hor

    @property
    def fiber2_vert(self) -> 'Fiber2Vert07453D00':
        return self._fiber2_vert

    @property
    def uv_outcpl(self) -> 'UvOutcpl07454000':
        return self._uv_outcpl

    @property
    def uv_cryst(self) -> 'UvCryst07453Fa0':
        return self._uv_cryst


class Ta1Hor07456E80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta1Vert07456Ee0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta2Hor074567C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Ta2Vert074566A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg1Hor07457120:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg1Vert074571E0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg2Hor07456640:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Shg2Vert07456880:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg1Hor07456940:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg1Vert07456Be0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg2Hor07457420:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fhg2Vert074575A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber1Hor074572A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber1Vert07457300:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber2Hor074573C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Fiber2Vert07453D00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class UvOutcpl07454000:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class UvCryst07453Fa0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._value = MutableDecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'MutableDecopInteger':
        return self._value


class Pd07453F40:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._dl = Dl07453B20(client, name + ':dl')
        self._amp = Amp07454060(client, name + ':amp')
        self._fiber = Fiber074539A0(client, name + ':fiber')
        self._shg = Shg07453B80(client, name + ':shg')
        self._shg_input = ShgInput074537C0(client, name + ':shg-input')
        self._shg_int = ShgInt07453Ee0(client, name + ':shg-int')
        self._shg_pdh_dc = ShgPdhDc07453820(client, name + ':shg-pdh-dc')
        self._shg_pdh_rf = ShgPdhRf07453880(client, name + ':shg-pdh-rf')
        self._fhg = Fhg07453Be0(client, name + ':fhg')
        self._fhg_int = FhgInt07454180(client, name + ':fhg-int')
        self._fhg_pdh_dc = FhgPdhDc07453D60(client, name + ':fhg-pdh-dc')
        self._fhg_pdh_rf = FhgPdhRf07453640(client, name + ':fhg-pdh-rf')

    @property
    def dl(self) -> 'Dl07453B20':
        return self._dl

    @property
    def amp(self) -> 'Amp07454060':
        return self._amp

    @property
    def fiber(self) -> 'Fiber074539A0':
        return self._fiber

    @property
    def shg(self) -> 'Shg07453B80':
        return self._shg

    @property
    def shg_input(self) -> 'ShgInput074537C0':
        return self._shg_input

    @property
    def shg_int(self) -> 'ShgInt07453Ee0':
        return self._shg_int

    @property
    def shg_pdh_dc(self) -> 'ShgPdhDc07453820':
        return self._shg_pdh_dc

    @property
    def shg_pdh_rf(self) -> 'ShgPdhRf07453880':
        return self._shg_pdh_rf

    @property
    def fhg(self) -> 'Fhg07453Be0':
        return self._fhg

    @property
    def fhg_int(self) -> 'FhgInt07454180':
        return self._fhg_int

    @property
    def fhg_pdh_dc(self) -> 'FhgPdhDc07453D60':
        return self._fhg_pdh_dc

    @property
    def fhg_pdh_rf(self) -> 'FhgPdhRf07453640':
        return self._fhg_pdh_rf


class Dl07453B20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Amp07454060:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Fiber074539A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Shg07453B80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInput074537C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInt07453Ee0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class ShgPdhDc07453820:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class ShgPdhRf07453880:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = MutableDecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'MutableDecopReal':
        return self._gain


class Fhg07453Be0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class FhgInt07454180:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class FhgPdhDc07453D60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class FhgPdhRf07453640:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = MutableDecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'MutableDecopReal':
        return self._gain


class PowerOptimization074542A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ongoing = DecopBoolean(client, name + ':ongoing')
        self._progress = DecopInteger(client, name + ':progress')
        self._status = DecopInteger(client, name + ':status')
        self._status_string = DecopString(client, name + ':status-string')
        self._shg_advanced = MutableDecopBoolean(client, name + ':shg-advanced')
        self._stage1 = Stage107454De0(client, name + ':stage1')
        self._stage2 = Stage207454D80(client, name + ':stage2')
        self._stage3 = Stage307454540(client, name + ':stage3')
        self._stage4 = Stage4074543C0(client, name + ':stage4')
        self._stage5 = Stage507454Cc0(client, name + ':stage5')
        self._progress_data_amp = DecopBinary(client, name + ':progress-data-amp')
        self._progress_data_shg = DecopBinary(client, name + ':progress-data-shg')
        self._progress_data_fiber = DecopBinary(client, name + ':progress-data-fiber')
        self._progress_data_fhg = DecopBinary(client, name + ':progress-data-fhg')
        self._abort = MutableDecopBoolean(client, name + ':abort')

    @property
    def ongoing(self) -> 'DecopBoolean':
        return self._ongoing

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_string(self) -> 'DecopString':
        return self._status_string

    @property
    def shg_advanced(self) -> 'MutableDecopBoolean':
        return self._shg_advanced

    @property
    def stage1(self) -> 'Stage107454De0':
        return self._stage1

    @property
    def stage2(self) -> 'Stage207454D80':
        return self._stage2

    @property
    def stage3(self) -> 'Stage307454540':
        return self._stage3

    @property
    def stage4(self) -> 'Stage4074543C0':
        return self._stage4

    @property
    def stage5(self) -> 'Stage507454Cc0':
        return self._stage5

    @property
    def progress_data_amp(self) -> 'DecopBinary':
        return self._progress_data_amp

    @property
    def progress_data_shg(self) -> 'DecopBinary':
        return self._progress_data_shg

    @property
    def progress_data_fiber(self) -> 'DecopBinary':
        return self._progress_data_fiber

    @property
    def progress_data_fhg(self) -> 'DecopBinary':
        return self._progress_data_fhg

    @property
    def abort(self) -> 'MutableDecopBoolean':
        return self._abort

    def start_optimization_all(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-all', input_stream=None, output_type=None, return_type=None)

    def start_optimization_amp(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-amp', input_stream=None, output_type=None, return_type=None)

    def start_optimization_shg(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-shg', input_stream=None, output_type=None, return_type=None)

    def start_optimization_fiber(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-fiber', input_stream=None, output_type=None, return_type=None)

    def start_optimization_fhg(self) -> None:
        self.__client.exec(self.__name + ':start-optimization-fhg', input_stream=None, output_type=None, return_type=None)


class Stage107454De0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input07454A80(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input07454A80':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input07454A80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage207454D80:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input07454240(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input07454240':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input07454240:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage307454540:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input07454C00(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input07454C00':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input07454C00:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage4074543C0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input07454C60(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input07454C60':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input07454C60:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class Stage507454Cc0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input07454780(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = MutableDecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = MutableDecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = MutableDecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input07454780':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'MutableDecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'MutableDecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'MutableDecopInteger':
        return self._regress_tolerance

    def start_optimization(self) -> None:
        self.__client.exec(self.__name + ':start-optimization', input_stream=None, output_type=None, return_type=None)


class Input07454780:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class AutoNlo07454D20:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._automatic_mode = DecopBoolean(client, name + ':automatic-mode')
        self._laser_on = MutableDecopBoolean(client, name + ':laser-on')
        self._emission = DecopBoolean(client, name + ':emission')
        self._operation_time_master = DecopReal(client, name + ':operation-time-master')
        self._operation_time_amplifier = DecopReal(client, name + ':operation-time-amplifier')
        self._operation_time_cavity = DecopReal(client, name + ':operation-time-cavity')
        self._amplifier_current_margin = DecopReal(client, name + ':amplifier-current-margin')

    @property
    def automatic_mode(self) -> 'DecopBoolean':
        return self._automatic_mode

    @property
    def laser_on(self) -> 'MutableDecopBoolean':
        return self._laser_on

    @property
    def emission(self) -> 'DecopBoolean':
        return self._emission

    @property
    def operation_time_master(self) -> 'DecopReal':
        return self._operation_time_master

    @property
    def operation_time_amplifier(self) -> 'DecopReal':
        return self._operation_time_amplifier

    @property
    def operation_time_cavity(self) -> 'DecopReal':
        return self._operation_time_cavity

    @property
    def amplifier_current_margin(self) -> 'DecopReal':
        return self._amplifier_current_margin

    def perform_single_mode_optimization(self) -> None:
        self.__client.exec(self.__name + ':perform-single-mode-optimization', input_stream=None, output_type=None, return_type=None)

    def perform_auto_align(self) -> None:
        self.__client.exec(self.__name + ':perform-auto-align', input_stream=None, output_type=None, return_type=None)


class Shg074548A0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc07454900(client, name + ':tc')
        self._pc = Pc06Fbf3F0(client, name + ':pc')
        self._scan = Scan06Fbecd0(client, name + ':scan')
        self._scope = Scope06Fbf2D0(client, name + ':scope')
        self._lock = Lock06Fbea90(client, name + ':lock')
        self._factory_settings = FactorySettings06Fbf930(client, name + ':factory-settings')

    @property
    def tc(self) -> 'Tc07454900':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fbf3F0':
        return self._pc

    @property
    def scan(self) -> 'Scan06Fbecd0':
        return self._scan

    @property
    def scope(self) -> 'Scope06Fbf2D0':
        return self._scope

    @property
    def lock(self) -> 'Lock06Fbea90':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings06Fbf930':
        return self._factory_settings


class Tc07454900:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fbee50(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fbebb0(client, name + ':t-loop')
        self._limits = Limits06Fbed90(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fbee50':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fbebb0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fbed90':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fbee50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop06Fbebb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits06Fbed90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc06Fbf3F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput06Fbf450(client, name + ':external-input')
        self._output_filter = OutputFilter06Fbe9D0(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput06Fbf450':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter06Fbe9D0':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput06Fbf450:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter06Fbe9D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Scan06Fbecd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset


class Scope06Fbf2D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel106Fbed30(client, name + ':channel1')
        self._channel2 = Channel206Fbf150(client, name + ':channel2')
        self._channelx = Channelx06Fbe910(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel106Fbed30':
        return self._channel1

    @property
    def channel2(self) -> 'Channel206Fbf150':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx06Fbe910':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel106Fbed30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel206Fbf150:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx06Fbe910:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock06Fbea90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock06Fbf270(client, name + ':relock')
        self._window = Window06Fbf390(client, name + ':window')
        self._pid1 = Pid106Fbefd0(client, name + ':pid1')
        self._pid2 = Pid206Fbf0F0(client, name + ':pid2')
        self._analog_dl_gain = AnalogDlGain06Fbf8D0(client, name + ':analog-dl-gain')
        self._local_oscillator = LocalOscillator06Fbfc90(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = MutableDecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = MutableDecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock06Fbf270':
        return self._relock

    @property
    def window(self) -> 'Window06Fbf390':
        return self._window

    @property
    def pid1(self) -> 'Pid106Fbefd0':
        return self._pid1

    @property
    def pid2(self) -> 'Pid206Fbf0F0':
        return self._pid2

    @property
    def analog_dl_gain(self) -> 'AnalogDlGain06Fbf8D0':
        return self._analog_dl_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator06Fbfc90':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock06Fbf270:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Window06Fbf390:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._threshold = MutableDecopReal(client, name + ':threshold')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration06Fbedf0(client, name + ':calibration')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'MutableDecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration06Fbedf0':
        return self._calibration


class Calibration06Fbedf0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid106Fbefd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain06Fbf030(client, name + ':gain')

    @property
    def gain(self) -> 'Gain06Fbf030':
        return self._gain


class Gain06Fbf030:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class Pid206Fbf0F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain06Fbf4B0(client, name + ':gain')

    @property
    def gain(self) -> 'Gain06Fbf4B0':
        return self._gain


class Gain06Fbf4B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class AnalogDlGain06Fbf8D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain


class LocalOscillator06Fbfc90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._use_external_oscillator = MutableDecopBoolean(client, name + ':use-external-oscillator')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._attenuation_raw = MutableDecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def use_external_oscillator(self) -> 'MutableDecopBoolean':
        return self._use_external_oscillator

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'MutableDecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    def auto_pdh(self) -> None:
        self.__client.exec(self.__name + ':auto-pdh', input_stream=None, output_type=None, return_type=None)


class FactorySettings06Fbf930:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fbfa50(client, name + ':tc')
        self._pc = Pc06Fbf570(client, name + ':pc')
        self._pd = Pd06Fbfdb0(client, name + ':pd')
        self._lock = Lock06Fbf810(client, name + ':lock')

    @property
    def tc(self) -> 'Tc06Fbfa50':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fbf570':
        return self._pc

    @property
    def pd(self) -> 'Pd06Fbfdb0':
        return self._pd

    @property
    def lock(self) -> 'Lock06Fbf810':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Tc06Fbfa50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc06Fbf570:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd06Fbfdb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg06Fbfb70(client, name + ':shg')
        self._shg_input = ShgInput06Fbfb10(client, name + ':shg-input')
        self._fiber = Fiber06Fbf630(client, name + ':fiber')
        self._int = Int06Fbf7B0(client, name + ':int')
        self._pdh_dc = PdhDc06Fbf5D0(client, name + ':pdh-dc')
        self._pdh_rf = PdhRf06Fbfe70(client, name + ':pdh-rf')

    @property
    def shg(self) -> 'Shg06Fbfb70':
        return self._shg

    @property
    def shg_input(self) -> 'ShgInput06Fbfb10':
        return self._shg_input

    @property
    def fiber(self) -> 'Fiber06Fbf630':
        return self._fiber

    @property
    def int(self) -> 'Int06Fbf7B0':
        return self._int

    @property
    def pdh_dc(self) -> 'PdhDc06Fbf5D0':
        return self._pdh_dc

    @property
    def pdh_rf(self) -> 'PdhRf06Fbfe70':
        return self._pdh_rf


class Shg06Fbfb70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class ShgInput06Fbfb10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Fiber06Fbf630:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Int06Fbf7B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhDc06Fbf5D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhRf06Fbfe70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class Lock06Fbf810:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock06Fbfc30(client, name + ':relock')
        self._window = Window06Fbfe10(client, name + ':window')
        self._pid1_gain = Pid1Gain06Fbfed0(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain06Fbf690(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator06Fbff30(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock06Fbfc30':
        return self._relock

    @property
    def window(self) -> 'Window06Fbfe10':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain06Fbfed0':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain06Fbf690':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator06Fbff30':
        return self._local_oscillator


class Relock06Fbfc30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window06Fbfe10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain06Fbfed0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain06Fbf690:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator06Fbff30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class Fhg06Fbf870:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fbf9F0(client, name + ':tc')
        self._pc = Pc06Fc0410(client, name + ':pc')
        self._scan = Scan06Fc0530(client, name + ':scan')
        self._scope = Scope06Fc0290(client, name + ':scope')
        self._lock = Lock06Fc0830(client, name + ':lock')
        self._factory_settings = FactorySettings06Fc12B0(client, name + ':factory-settings')

    @property
    def tc(self) -> 'Tc06Fbf9F0':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fc0410':
        return self._pc

    @property
    def scan(self) -> 'Scan06Fc0530':
        return self._scan

    @property
    def scope(self) -> 'Scope06Fc0290':
        return self._scope

    @property
    def lock(self) -> 'Lock06Fc0830':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings06Fc12B0':
        return self._factory_settings


class Tc06Fbf9F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = MutableDecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fbff90(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fc0230(client, name + ':t-loop')
        self._limits = Limits06Fc0B30(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'MutableDecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fbff90':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fc0230':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fc0B30':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fbff90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class TLoop06Fc0230:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = MutableDecopReal(client, name + ':p-gain')
        self._i_gain = MutableDecopReal(client, name + ':i-gain')
        self._d_gain = MutableDecopReal(client, name + ':d-gain')
        self._ok_tolerance = MutableDecopReal(client, name + ':ok-tolerance')
        self._ok_time = MutableDecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'MutableDecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'MutableDecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'MutableDecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'MutableDecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'MutableDecopReal':
        return self._ok_time


class Limits06Fc0B30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = MutableDecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'MutableDecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc06Fc0410:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._voltage_set = MutableDecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = MutableDecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput06Fc0C50(client, name + ':external-input')
        self._output_filter = OutputFilter06Fc0470(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'MutableDecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'MutableDecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput06Fc0C50':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter06Fc0470':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput06Fc0C50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._factor = MutableDecopReal(client, name + ':factor')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def factor(self) -> 'MutableDecopReal':
        return self._factor

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class OutputFilter06Fc0470:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = MutableDecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = MutableDecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'MutableDecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'MutableDecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Scan06Fc0530:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._offset = MutableDecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'MutableDecopReal':
        return self._offset


class Scope06Fc0290:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = MutableDecopInteger(client, name + ':variant')
        self._update_rate = MutableDecopInteger(client, name + ':update-rate')
        self._channel1 = Channel106Fc0650(client, name + ':channel1')
        self._channel2 = Channel206Fc02F0(client, name + ':channel2')
        self._channelx = Channelx06Fc0710(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'MutableDecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'MutableDecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel106Fc0650':
        return self._channel1

    @property
    def channel2(self) -> 'Channel206Fc02F0':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx06Fc0710':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel106Fc0650:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel206Fc02F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = MutableDecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'MutableDecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx06Fc0710:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = MutableDecopInteger(client, name + ':xy-signal')
        self._scope_timescale = MutableDecopReal(client, name + ':scope-timescale')
        self._spectrum_range = MutableDecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = MutableDecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'MutableDecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'MutableDecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'MutableDecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'MutableDecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock06Fc0830:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = MutableDecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = MutableDecopInteger(client, name + ':pid-selection')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._relock = Relock06Fc07D0(client, name + ':relock')
        self._window = Window06Fc05F0(client, name + ':window')
        self._pid1 = Pid106Fc08F0(client, name + ':pid1')
        self._pid2 = Pid206Fc0950(client, name + ':pid2')
        self._local_oscillator = LocalOscillator06Fc0A70(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = MutableDecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = MutableDecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'MutableDecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'MutableDecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock06Fc07D0':
        return self._relock

    @property
    def window(self) -> 'Window06Fc05F0':
        return self._window

    @property
    def pid1(self) -> 'Pid106Fc08F0':
        return self._pid1

    @property
    def pid2(self) -> 'Pid206Fc0950':
        return self._pid2

    @property
    def local_oscillator(self) -> 'LocalOscillator06Fc0A70':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'MutableDecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock06Fc07D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._frequency = MutableDecopReal(client, name + ':frequency')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._delay = MutableDecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'MutableDecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'MutableDecopReal':
        return self._delay


class Window06Fc05F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._threshold = MutableDecopReal(client, name + ':threshold')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration06Fc0890(client, name + ':calibration')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'MutableDecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration06Fc0890':
        return self._calibration


class Calibration06Fc0890:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid106Fc08F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain06Fc0A10(client, name + ':gain')

    @property
    def gain(self) -> 'Gain06Fc0A10':
        return self._gain


class Gain06Fc0A10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class Pid206Fc0950:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain06Fc09B0(client, name + ':gain')

    @property
    def gain(self) -> 'Gain06Fc09B0':
        return self._gain


class Gain06Fc09B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')
        self._i_cutoff = MutableDecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = MutableDecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'MutableDecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'MutableDecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator06Fc0A70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._amplitude = MutableDecopReal(client, name + ':amplitude')
        self._attenuation_raw = MutableDecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = MutableDecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def amplitude(self) -> 'MutableDecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'MutableDecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'MutableDecopReal':
        return self._phase_shift

    def auto_pdh(self) -> None:
        self.__client.exec(self.__name + ':auto-pdh', input_stream=None, output_type=None, return_type=None)


class FactorySettings06Fc12B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fc0Cb0(client, name + ':tc')
        self._pc = Pc06Fc0E30(client, name + ':pc')
        self._pd = Pd06Fc10D0(client, name + ':pd')
        self._lock = Lock06Fc1850(client, name + ':lock')

    @property
    def tc(self) -> 'Tc06Fc0Cb0':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fc0E30':
        return self._pc

    @property
    def pd(self) -> 'Pd06Fc10D0':
        return self._pd

    @property
    def lock(self) -> 'Lock06Fc1850':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class Tc06Fc0Cb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc06Fc0E30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd06Fc10D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._fhg = Fhg06Fc0D10(client, name + ':fhg')
        self._int = Int06Fc1190(client, name + ':int')
        self._pdh_dc = PdhDc06Fc11F0(client, name + ':pdh-dc')
        self._pdh_rf = PdhRf06Fc1310(client, name + ':pdh-rf')

    @property
    def fhg(self) -> 'Fhg06Fc0D10':
        return self._fhg

    @property
    def int(self) -> 'Int06Fc1190':
        return self._int

    @property
    def pdh_dc(self) -> 'PdhDc06Fc11F0':
        return self._pdh_dc

    @property
    def pdh_rf(self) -> 'PdhRf06Fc1310':
        return self._pdh_rf


class Fhg06Fc0D10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class Int06Fc1190:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhDc06Fc11F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PdhRf06Fc1310:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class Lock06Fc1850:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock06Fc0F50(client, name + ':relock')
        self._window = Window06Fc1430(client, name + ':window')
        self._pid1_gain = Pid1Gain06Fc0Dd0(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain06Fc17F0(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator06Fc14F0(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock06Fc0F50':
        return self._relock

    @property
    def window(self) -> 'Window06Fc1430':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain06Fc0Dd0':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain06Fc17F0':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator06Fc14F0':
        return self._local_oscillator


class Relock06Fc0F50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window06Fc1430:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain06Fc0Dd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain06Fc17F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator06Fc14F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class Uv06Fc1010:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pump = Pump06Fc1490(client, name + ':pump')
        self._eom = Eom06Fc1070(client, name + ':eom')
        self._cavity = Cavity06Fc1D90(client, name + ':cavity')
        self._crystal = Crystal06Fc1D30(client, name + ':crystal')
        self._servo = Servo06Fc2630(client, name + ':servo')
        self._pd = Pd07350C70(client, name + ':pd')
        self._power_optimization = PowerOptimization07351030(client, name + ':power-optimization')
        self._power_stabilization = PowerStabilization073508B0(client, name + ':power-stabilization')
        self._scan = Scan07351270(client, name + ':scan')
        self._scope = Scope07351330(client, name + ':scope')
        self._lock = Lock07351750(client, name + ':lock')
        self._factory_settings = FactorySettings07351B70(client, name + ':factory-settings')
        self._status_parameters = StatusParameters07352770(client, name + ':status-parameters')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._hwp_transmittance = DecopReal(client, name + ':hwp-transmittance')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._specs_fulfilled = DecopBoolean(client, name + ':specs-fulfilled')
        self._error = DecopInteger(client, name + ':error')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._remaining_optics_spots = DecopInteger(client, name + ':remaining-optics-spots')
        self._baseplate_temperature = DecopReal(client, name + ':baseplate-temperature')
        self._ssw_ver = DecopString(client, name + ':ssw-ver')

    @property
    def pump(self) -> 'Pump06Fc1490':
        return self._pump

    @property
    def eom(self) -> 'Eom06Fc1070':
        return self._eom

    @property
    def cavity(self) -> 'Cavity06Fc1D90':
        return self._cavity

    @property
    def crystal(self) -> 'Crystal06Fc1D30':
        return self._crystal

    @property
    def servo(self) -> 'Servo06Fc2630':
        return self._servo

    @property
    def pd(self) -> 'Pd07350C70':
        return self._pd

    @property
    def power_optimization(self) -> 'PowerOptimization07351030':
        return self._power_optimization

    @property
    def power_stabilization(self) -> 'PowerStabilization073508B0':
        return self._power_stabilization

    @property
    def scan(self) -> 'Scan07351270':
        return self._scan

    @property
    def scope(self) -> 'Scope07351330':
        return self._scope

    @property
    def lock(self) -> 'Lock07351750':
        return self._lock

    @property
    def factory_settings(self) -> 'FactorySettings07351B70':
        return self._factory_settings

    @property
    def status_parameters(self) -> 'StatusParameters07352770':
        return self._status_parameters

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def hwp_transmittance(self) -> 'DecopReal':
        return self._hwp_transmittance

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def specs_fulfilled(self) -> 'DecopBoolean':
        return self._specs_fulfilled

    @property
    def error(self) -> 'DecopInteger':
        return self._error

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def remaining_optics_spots(self) -> 'DecopInteger':
        return self._remaining_optics_spots

    @property
    def baseplate_temperature(self) -> 'DecopReal':
        return self._baseplate_temperature

    @property
    def ssw_ver(self) -> 'DecopString':
        return self._ssw_ver

    def perform_optimization(self) -> None:
        self.__client.exec(self.__name + ':perform-optimization', input_stream=None, output_type=None, return_type=None)

    def perform_optics_shift(self) -> None:
        self.__client.exec(self.__name + ':perform-optics-shift', input_stream=None, output_type=None, return_type=None)

    def clear_errors(self) -> None:
        self.__client.exec(self.__name + ':clear-errors', input_stream=None, output_type=None, return_type=None)


class Pump06Fc1490:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._tc_status = DecopInteger(client, name + ':tc-status')
        self._tc_status_txt = DecopString(client, name + ':tc-status-txt')
        self._error_code = DecopInteger(client, name + ':error-code')
        self._error_txt = DecopString(client, name + ':error-txt')
        self._operation_time = DecopReal(client, name + ':operation-time')
        self._power_set = DecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_max = DecopReal(client, name + ':power-max')
        self._power_margin = DecopReal(client, name + ':power-margin')
        self._current_act = DecopReal(client, name + ':current-act')
        self._current_max = DecopReal(client, name + ':current-max')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def tc_status(self) -> 'DecopInteger':
        return self._tc_status

    @property
    def tc_status_txt(self) -> 'DecopString':
        return self._tc_status_txt

    @property
    def error_code(self) -> 'DecopInteger':
        return self._error_code

    @property
    def error_txt(self) -> 'DecopString':
        return self._error_txt

    @property
    def operation_time(self) -> 'DecopReal':
        return self._operation_time

    @property
    def power_set(self) -> 'DecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def power_margin(self) -> 'DecopReal':
        return self._power_margin

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max


class Eom06Fc1070:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fc1790(client, name + ':tc')

    @property
    def tc(self) -> 'Tc06Fc1790':
        return self._tc


class Tc06Fc1790:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fc1970(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fc1Bb0(client, name + ':t-loop')
        self._limits = Limits06Fc19D0(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fc1970':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fc1Bb0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fc19D0':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fc1970:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop06Fc1Bb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits06Fc19D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Cavity06Fc1D90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fc2210(client, name + ':tc')
        self._pc = Pc06Fc1C70(client, name + ':pc')

    @property
    def tc(self) -> 'Tc06Fc2210':
        return self._tc

    @property
    def pc(self) -> 'Pc06Fc1C70':
        return self._pc


class Tc06Fc2210:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fc2090(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fc22D0(client, name + ':t-loop')
        self._limits = Limits06Fc1C10(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fc2090':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fc22D0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fc1C10':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fc2090:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop06Fc22D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits06Fc1C10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class Pc06Fc1C70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._voltage_set = DecopReal(client, name + ':voltage-set')
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._voltage_set_dithering = DecopBoolean(client, name + ':voltage-set-dithering')
        self._external_input = ExternalInput06Fc2270(client, name + ':external-input')
        self._output_filter = OutputFilter06Fc2330(client, name + ':output-filter')
        self._voltage_act = DecopReal(client, name + ':voltage-act')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._heatsink_temp = DecopReal(client, name + ':heatsink-temp')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def voltage_set(self) -> 'DecopReal':
        return self._voltage_set

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def voltage_set_dithering(self) -> 'DecopBoolean':
        return self._voltage_set_dithering

    @property
    def external_input(self) -> 'ExternalInput06Fc2270':
        return self._external_input

    @property
    def output_filter(self) -> 'OutputFilter06Fc2330':
        return self._output_filter

    @property
    def voltage_act(self) -> 'DecopReal':
        return self._voltage_act

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def heatsink_temp(self) -> 'DecopReal':
        return self._heatsink_temp

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt


class ExternalInput06Fc2270:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class OutputFilter06Fc2330:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._slew_rate = DecopReal(client, name + ':slew-rate')
        self._slew_rate_enabled = DecopBoolean(client, name + ':slew-rate-enabled')
        self._slew_rate_limited = DecopBoolean(client, name + ':slew-rate-limited')

    @property
    def slew_rate(self) -> 'DecopReal':
        return self._slew_rate

    @property
    def slew_rate_enabled(self) -> 'DecopBoolean':
        return self._slew_rate_enabled

    @property
    def slew_rate_limited(self) -> 'DecopBoolean':
        return self._slew_rate_limited


class Crystal06Fc1D30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._tc = Tc06Fc18B0(client, name + ':tc')
        self._optics_shifters = OpticsShifters06Fc1910(client, name + ':optics-shifters')

    @property
    def tc(self) -> 'Tc06Fc18B0':
        return self._tc

    @property
    def optics_shifters(self) -> 'OpticsShifters06Fc1910':
        return self._optics_shifters


class Tc06Fc18B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._path = DecopString(client, name + ':path')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._temp_act = DecopReal(client, name + ':temp-act')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._external_input = ExternalInput06Fc1Eb0(client, name + ':external-input')
        self._ready = DecopBoolean(client, name + ':ready')
        self._fault = DecopBoolean(client, name + ':fault')
        self._status = DecopInteger(client, name + ':status')
        self._status_txt = DecopString(client, name + ':status-txt')
        self._t_loop = TLoop06Fc1Fd0(client, name + ':t-loop')
        self._limits = Limits06Fc2030(client, name + ':limits')
        self._current_set = DecopReal(client, name + ':current-set')
        self._current_act = DecopReal(client, name + ':current-act')
        self._temp_set_min = DecopReal(client, name + ':temp-set-min')
        self._temp_set_max = DecopReal(client, name + ':temp-set-max')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')

    @property
    def path(self) -> 'DecopString':
        return self._path

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def temp_act(self) -> 'DecopReal':
        return self._temp_act

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def external_input(self) -> 'ExternalInput06Fc1Eb0':
        return self._external_input

    @property
    def ready(self) -> 'DecopBoolean':
        return self._ready

    @property
    def fault(self) -> 'DecopBoolean':
        return self._fault

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_txt(self) -> 'DecopString':
        return self._status_txt

    @property
    def t_loop(self) -> 'TLoop06Fc1Fd0':
        return self._t_loop

    @property
    def limits(self) -> 'Limits06Fc2030':
        return self._limits

    @property
    def current_set(self) -> 'DecopReal':
        return self._current_set

    @property
    def current_act(self) -> 'DecopReal':
        return self._current_act

    @property
    def temp_set_min(self) -> 'DecopReal':
        return self._temp_set_min

    @property
    def temp_set_max(self) -> 'DecopReal':
        return self._temp_set_max

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit


class ExternalInput06Fc1Eb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._factor = DecopReal(client, name + ':factor')
        self._enabled = DecopBoolean(client, name + ':enabled')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def factor(self) -> 'DecopReal':
        return self._factor

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled


class TLoop06Fc1Fd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time


class Limits06Fc2030:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._timed_out = DecopBoolean(client, name + ':timed-out')
        self._out_of_range = DecopBoolean(client, name + ':out-of-range')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def timed_out(self) -> 'DecopBoolean':
        return self._timed_out

    @property
    def out_of_range(self) -> 'DecopBoolean':
        return self._out_of_range


class OpticsShifters06Fc1910:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._current_spot = DecopInteger(client, name + ':current-spot')
        self._remaining_spots = DecopInteger(client, name + ':remaining-spots')

    @property
    def current_spot(self) -> 'DecopInteger':
        return self._current_spot

    @property
    def remaining_spots(self) -> 'DecopInteger':
        return self._remaining_spots


class Servo06Fc2630:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg1_hor = Shg1Hor06Fc2570(client, name + ':shg1-hor')
        self._shg1_vert = Shg1Vert06Fc2810(client, name + ':shg1-vert')
        self._shg2_hor = Shg2Hor06Fc25D0(client, name + ':shg2-hor')
        self._shg2_vert = Shg2Vert06Fc26F0(client, name + ':shg2-vert')
        self._hwp = Hwp07350Cd0(client, name + ':hwp')
        self._lens = Lens07350B50(client, name + ':lens')
        self._outcpl = Outcpl07350Bb0(client, name + ':outcpl')
        self._cryst = Cryst07350910(client, name + ':cryst')
        self._comp_hor = CompHor073509D0(client, name + ':comp-hor')
        self._comp_vert = CompVert07350C10(client, name + ':comp-vert')

    @property
    def shg1_hor(self) -> 'Shg1Hor06Fc2570':
        return self._shg1_hor

    @property
    def shg1_vert(self) -> 'Shg1Vert06Fc2810':
        return self._shg1_vert

    @property
    def shg2_hor(self) -> 'Shg2Hor06Fc25D0':
        return self._shg2_hor

    @property
    def shg2_vert(self) -> 'Shg2Vert06Fc26F0':
        return self._shg2_vert

    @property
    def hwp(self) -> 'Hwp07350Cd0':
        return self._hwp

    @property
    def lens(self) -> 'Lens07350B50':
        return self._lens

    @property
    def outcpl(self) -> 'Outcpl07350Bb0':
        return self._outcpl

    @property
    def cryst(self) -> 'Cryst07350910':
        return self._cryst

    @property
    def comp_hor(self) -> 'CompHor073509D0':
        return self._comp_hor

    @property
    def comp_vert(self) -> 'CompVert07350C10':
        return self._comp_vert


class Shg1Hor06Fc2570:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg1Vert06Fc2810:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg2Hor06Fc25D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Shg2Vert06Fc26F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Hwp07350Cd0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Lens07350B50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Outcpl07350Bb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Cryst07350910:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class CompHor073509D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class CompVert07350C10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._display_name = DecopString(client, name + ':display-name')
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._value = DecopInteger(client, name + ':value')

    @property
    def display_name(self) -> 'DecopString':
        return self._display_name

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def value(self) -> 'DecopInteger':
        return self._value


class Pd07350C70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg07350F10(client, name + ':shg')
        self._pdh_rf = PdhRf07350Eb0(client, name + ':pdh-rf')
        self._pdh_dc = PdhDc07350F70(client, name + ':pdh-dc')

    @property
    def shg(self) -> 'Shg07350F10':
        return self._shg

    @property
    def pdh_rf(self) -> 'PdhRf07350Eb0':
        return self._pdh_rf

    @property
    def pdh_dc(self) -> 'PdhDc07350F70':
        return self._pdh_dc


class Shg07350F10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class PdhRf07350Eb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._gain = DecopReal(client, name + ':gain')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class PdhDc07350F70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class PowerOptimization07351030:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._ongoing = DecopBoolean(client, name + ':ongoing')
        self._status = DecopInteger(client, name + ':status')
        self._status_string = DecopString(client, name + ':status-string')
        self._cavity = Cavity07350970(client, name + ':cavity')
        self._progress_data = DecopBinary(client, name + ':progress-data')
        self._abort = DecopBoolean(client, name + ':abort')

    @property
    def ongoing(self) -> 'DecopBoolean':
        return self._ongoing

    @property
    def status(self) -> 'DecopInteger':
        return self._status

    @property
    def status_string(self) -> 'DecopString':
        return self._status_string

    @property
    def cavity(self) -> 'Cavity07350970':
        return self._cavity

    @property
    def progress_data(self) -> 'DecopBinary':
        return self._progress_data

    @property
    def abort(self) -> 'DecopBoolean':
        return self._abort


class Cavity07350970:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input = Input073510F0(client, name + ':input')
        self._progress = DecopInteger(client, name + ':progress')
        self._optimization_in_progress = DecopBoolean(client, name + ':optimization-in-progress')
        self._restore_on_abort = DecopBoolean(client, name + ':restore-on-abort')
        self._restore_on_regress = DecopBoolean(client, name + ':restore-on-regress')
        self._regress_tolerance = DecopInteger(client, name + ':regress-tolerance')

    @property
    def input(self) -> 'Input073510F0':
        return self._input

    @property
    def progress(self) -> 'DecopInteger':
        return self._progress

    @property
    def optimization_in_progress(self) -> 'DecopBoolean':
        return self._optimization_in_progress

    @property
    def restore_on_abort(self) -> 'DecopBoolean':
        return self._restore_on_abort

    @property
    def restore_on_regress(self) -> 'DecopBoolean':
        return self._restore_on_regress

    @property
    def regress_tolerance(self) -> 'DecopInteger':
        return self._regress_tolerance


class Input073510F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._value_calibrated = DecopReal(client, name + ':value-calibrated')

    @property
    def value_calibrated(self) -> 'DecopReal':
        return self._value_calibrated


class PowerStabilization073508B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._gain = Gain07350A30(client, name + ':gain')
        self._power_set = DecopReal(client, name + ':power-set')
        self._power_act = DecopReal(client, name + ':power-act')
        self._power_min = DecopReal(client, name + ':power-min')
        self._power_max = DecopReal(client, name + ':power-max')
        self._state = DecopInteger(client, name + ':state')
        self._update_strategy = DecopInteger(client, name + ':update-strategy')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain07350A30':
        return self._gain

    @property
    def power_set(self) -> 'DecopReal':
        return self._power_set

    @property
    def power_act(self) -> 'DecopReal':
        return self._power_act

    @property
    def power_min(self) -> 'DecopReal':
        return self._power_min

    @property
    def power_max(self) -> 'DecopReal':
        return self._power_max

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def update_strategy(self) -> 'DecopInteger':
        return self._update_strategy


class Gain07350A30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d


class Scan07351270:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._offset = DecopReal(client, name + ':offset')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def offset(self) -> 'DecopReal':
        return self._offset


class Scope07351330:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._variant = DecopInteger(client, name + ':variant')
        self._update_rate = DecopInteger(client, name + ':update-rate')
        self._channel1 = Channel1073517B0(client, name + ':channel1')
        self._channel2 = Channel207351450(client, name + ':channel2')
        self._channelx = Channelx07351Cf0(client, name + ':channelx')
        self._timescale = DecopReal(client, name + ':timescale')
        self._data = DecopBinary(client, name + ':data')

    @property
    def variant(self) -> 'DecopInteger':
        return self._variant

    @property
    def update_rate(self) -> 'DecopInteger':
        return self._update_rate

    @property
    def channel1(self) -> 'Channel1073517B0':
        return self._channel1

    @property
    def channel2(self) -> 'Channel207351450':
        return self._channel2

    @property
    def channelx(self) -> 'Channelx07351Cf0':
        return self._channelx

    @property
    def timescale(self) -> 'DecopReal':
        return self._timescale

    @property
    def data(self) -> 'DecopBinary':
        return self._data


class Channel1073517B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channel207351450:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._signal = DecopInteger(client, name + ':signal')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def signal(self) -> 'DecopInteger':
        return self._signal

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Channelx07351Cf0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._xy_signal = DecopInteger(client, name + ':xy-signal')
        self._scope_timescale = DecopReal(client, name + ':scope-timescale')
        self._spectrum_range = DecopReal(client, name + ':spectrum-range')
        self._spectrum_omit_dc = DecopBoolean(client, name + ':spectrum-omit-dc')
        self._unit = DecopString(client, name + ':unit')
        self._name = DecopString(client, name + ':name')

    @property
    def xy_signal(self) -> 'DecopInteger':
        return self._xy_signal

    @property
    def scope_timescale(self) -> 'DecopReal':
        return self._scope_timescale

    @property
    def spectrum_range(self) -> 'DecopReal':
        return self._spectrum_range

    @property
    def spectrum_omit_dc(self) -> 'DecopBoolean':
        return self._spectrum_omit_dc

    @property
    def unit(self) -> 'DecopString':
        return self._unit

    @property
    def name(self) -> 'DecopString':
        return self._name


class Lock07351750:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._state = DecopInteger(client, name + ':state')
        self._state_txt = DecopString(client, name + ':state-txt')
        self._lock_enabled = DecopBoolean(client, name + ':lock-enabled')
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock07351630(client, name + ':relock')
        self._window = Window07351B10(client, name + ':window')
        self._pid1 = Pid1073518D0(client, name + ':pid1')
        self._pid2 = Pid207351E10(client, name + ':pid2')
        self._analog_dl_gain = AnalogDlGain07351810(client, name + ':analog-dl-gain')
        self._local_oscillator = LocalOscillator07351C30(client, name + ':local-oscillator')
        self._cavity_fast_pzt_voltage = DecopReal(client, name + ':cavity-fast-pzt-voltage')
        self._cavity_slow_pzt_voltage = DecopReal(client, name + ':cavity-slow-pzt-voltage')
        self._background_trace = DecopBinary(client, name + ':background-trace')

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    @property
    def lock_enabled(self) -> 'DecopBoolean':
        return self._lock_enabled

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock07351630':
        return self._relock

    @property
    def window(self) -> 'Window07351B10':
        return self._window

    @property
    def pid1(self) -> 'Pid1073518D0':
        return self._pid1

    @property
    def pid2(self) -> 'Pid207351E10':
        return self._pid2

    @property
    def analog_dl_gain(self) -> 'AnalogDlGain07351810':
        return self._analog_dl_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator07351C30':
        return self._local_oscillator

    @property
    def cavity_fast_pzt_voltage(self) -> 'DecopReal':
        return self._cavity_fast_pzt_voltage

    @property
    def cavity_slow_pzt_voltage(self) -> 'DecopReal':
        return self._cavity_slow_pzt_voltage

    @property
    def background_trace(self) -> 'DecopBinary':
        return self._background_trace


class Relock07351630:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window07351B10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')
        self._calibration = Calibration073514B0(client, name + ':calibration')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis

    @property
    def calibration(self) -> 'Calibration073514B0':
        return self._calibration


class Calibration073514B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name


class Pid1073518D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain07351D50(client, name + ':gain')

    @property
    def gain(self) -> 'Gain07351D50':
        return self._gain


class Gain07351D50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid207351E10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = Gain07351A50(client, name + ':gain')

    @property
    def gain(self) -> 'Gain07351A50':
        return self._gain


class Gain07351A50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class AnalogDlGain07351810:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._p_gain = DecopReal(client, name + ':p-gain')

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain


class LocalOscillator07351C30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._use_external_oscillator = DecopBoolean(client, name + ':use-external-oscillator')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._attenuation_raw = DecopInteger(client, name + ':attenuation-raw')
        self._phase_shift = DecopReal(client, name + ':phase-shift')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def use_external_oscillator(self) -> 'DecopBoolean':
        return self._use_external_oscillator

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def attenuation_raw(self) -> 'DecopInteger':
        return self._attenuation_raw

    @property
    def phase_shift(self) -> 'DecopReal':
        return self._phase_shift


class FactorySettings07351B70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._eom_tc = EomTc07351Db0(client, name + ':eom-tc')
        self._crystal_tc = CrystalTc07351Ab0(client, name + ':crystal-tc')
        self._cavity_tc = CavityTc07351C90(client, name + ':cavity-tc')
        self._pc = Pc07352650(client, name + ':pc')
        self._pd = Pd07352230(client, name + ':pd')
        self._lock = Lock07352590(client, name + ':lock')

    @property
    def eom_tc(self) -> 'EomTc07351Db0':
        return self._eom_tc

    @property
    def crystal_tc(self) -> 'CrystalTc07351Ab0':
        return self._crystal_tc

    @property
    def cavity_tc(self) -> 'CavityTc07351C90':
        return self._cavity_tc

    @property
    def pc(self) -> 'Pc07352650':
        return self._pc

    @property
    def pd(self) -> 'Pd07352230':
        return self._pd

    @property
    def lock(self) -> 'Lock07352590':
        return self._lock

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)


class EomTc07351Db0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class CrystalTc07351Ab0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class CavityTc07351C90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._temp_min = DecopReal(client, name + ':temp-min')
        self._temp_max = DecopReal(client, name + ':temp-max')
        self._temp_set = DecopReal(client, name + ':temp-set')
        self._temp_roc_limit = DecopReal(client, name + ':temp-roc-limit')
        self._temp_roc_enabled = DecopBoolean(client, name + ':temp-roc-enabled')
        self._current_max = DecopReal(client, name + ':current-max')
        self._current_min = DecopReal(client, name + ':current-min')
        self._p_gain = DecopReal(client, name + ':p-gain')
        self._i_gain = DecopReal(client, name + ':i-gain')
        self._d_gain = DecopReal(client, name + ':d-gain')
        self._c_gain = DecopReal(client, name + ':c-gain')
        self._ok_tolerance = DecopReal(client, name + ':ok-tolerance')
        self._ok_time = DecopReal(client, name + ':ok-time')
        self._timeout = DecopInteger(client, name + ':timeout')
        self._power_source = DecopInteger(client, name + ':power-source')
        self._ntc_series_resistance = DecopReal(client, name + ':ntc-series-resistance')

    @property
    def temp_min(self) -> 'DecopReal':
        return self._temp_min

    @property
    def temp_max(self) -> 'DecopReal':
        return self._temp_max

    @property
    def temp_set(self) -> 'DecopReal':
        return self._temp_set

    @property
    def temp_roc_limit(self) -> 'DecopReal':
        return self._temp_roc_limit

    @property
    def temp_roc_enabled(self) -> 'DecopBoolean':
        return self._temp_roc_enabled

    @property
    def current_max(self) -> 'DecopReal':
        return self._current_max

    @property
    def current_min(self) -> 'DecopReal':
        return self._current_min

    @property
    def p_gain(self) -> 'DecopReal':
        return self._p_gain

    @property
    def i_gain(self) -> 'DecopReal':
        return self._i_gain

    @property
    def d_gain(self) -> 'DecopReal':
        return self._d_gain

    @property
    def c_gain(self) -> 'DecopReal':
        return self._c_gain

    @property
    def ok_tolerance(self) -> 'DecopReal':
        return self._ok_tolerance

    @property
    def ok_time(self) -> 'DecopReal':
        return self._ok_time

    @property
    def timeout(self) -> 'DecopInteger':
        return self._timeout

    @property
    def power_source(self) -> 'DecopInteger':
        return self._power_source

    @property
    def ntc_series_resistance(self) -> 'DecopReal':
        return self._ntc_series_resistance


class Pc07352650:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._voltage_min = DecopReal(client, name + ':voltage-min')
        self._voltage_max = DecopReal(client, name + ':voltage-max')
        self._feedforward_enabled = DecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = DecopReal(client, name + ':feedforward-factor')
        self._capacitance = DecopReal(client, name + ':capacitance')
        self._scan_offset = DecopReal(client, name + ':scan-offset')
        self._scan_amplitude = DecopReal(client, name + ':scan-amplitude')
        self._scan_frequency = DecopReal(client, name + ':scan-frequency')

    @property
    def voltage_min(self) -> 'DecopReal':
        return self._voltage_min

    @property
    def voltage_max(self) -> 'DecopReal':
        return self._voltage_max

    @property
    def feedforward_enabled(self) -> 'DecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'DecopReal':
        return self._feedforward_factor

    @property
    def capacitance(self) -> 'DecopReal':
        return self._capacitance

    @property
    def scan_offset(self) -> 'DecopReal':
        return self._scan_offset

    @property
    def scan_amplitude(self) -> 'DecopReal':
        return self._scan_amplitude

    @property
    def scan_frequency(self) -> 'DecopReal':
        return self._scan_frequency


class Pd07352230:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._shg = Shg07352830(client, name + ':shg')
        self._pdh_rf = PdhRf07352530(client, name + ':pdh-rf')
        self._pdh_dc = PdhDc073526B0(client, name + ':pdh-dc')

    @property
    def shg(self) -> 'Shg07352830':
        return self._shg

    @property
    def pdh_rf(self) -> 'PdhRf07352530':
        return self._pdh_rf

    @property
    def pdh_dc(self) -> 'PdhDc073526B0':
        return self._pdh_dc


class Shg07352830:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')
        self._cal_factor = DecopReal(client, name + ':cal-factor')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'DecopReal':
        return self._cal_factor


class PdhRf07352530:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._gain = DecopReal(client, name + ':gain')

    @property
    def gain(self) -> 'DecopReal':
        return self._gain


class PdhDc073526B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._cal_offset = DecopReal(client, name + ':cal-offset')

    @property
    def cal_offset(self) -> 'DecopReal':
        return self._cal_offset


class Lock07352590:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._pid_selection = DecopInteger(client, name + ':pid-selection')
        self._setpoint = DecopReal(client, name + ':setpoint')
        self._relock = Relock073524D0(client, name + ':relock')
        self._window = Window073520B0(client, name + ':window')
        self._pid1_gain = Pid1Gain07352710(client, name + ':pid1-gain')
        self._pid2_gain = Pid2Gain07352170(client, name + ':pid2-gain')
        self._analog_p_gain = DecopReal(client, name + ':analog-p-gain')
        self._local_oscillator = LocalOscillator07352890(client, name + ':local-oscillator')

    @property
    def pid_selection(self) -> 'DecopInteger':
        return self._pid_selection

    @property
    def setpoint(self) -> 'DecopReal':
        return self._setpoint

    @property
    def relock(self) -> 'Relock073524D0':
        return self._relock

    @property
    def window(self) -> 'Window073520B0':
        return self._window

    @property
    def pid1_gain(self) -> 'Pid1Gain07352710':
        return self._pid1_gain

    @property
    def pid2_gain(self) -> 'Pid2Gain07352170':
        return self._pid2_gain

    @property
    def analog_p_gain(self) -> 'DecopReal':
        return self._analog_p_gain

    @property
    def local_oscillator(self) -> 'LocalOscillator07352890':
        return self._local_oscillator


class Relock073524D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._frequency = DecopReal(client, name + ':frequency')
        self._amplitude = DecopReal(client, name + ':amplitude')
        self._delay = DecopReal(client, name + ':delay')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def amplitude(self) -> 'DecopReal':
        return self._amplitude

    @property
    def delay(self) -> 'DecopReal':
        return self._delay


class Window073520B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = DecopInteger(client, name + ':input-channel')
        self._threshold = DecopReal(client, name + ':threshold')
        self._level_hysteresis = DecopReal(client, name + ':level-hysteresis')

    @property
    def input_channel(self) -> 'DecopInteger':
        return self._input_channel

    @property
    def threshold(self) -> 'DecopReal':
        return self._threshold

    @property
    def level_hysteresis(self) -> 'DecopReal':
        return self._level_hysteresis


class Pid1Gain07352710:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class Pid2Gain07352170:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = DecopReal(client, name + ':all')
        self._p = DecopReal(client, name + ':p')
        self._i = DecopReal(client, name + ':i')
        self._d = DecopReal(client, name + ':d')
        self._i_cutoff = DecopReal(client, name + ':i-cutoff')
        self._i_cutoff_enabled = DecopBoolean(client, name + ':i-cutoff-enabled')

    @property
    def all(self) -> 'DecopReal':
        return self._all

    @property
    def p(self) -> 'DecopReal':
        return self._p

    @property
    def i(self) -> 'DecopReal':
        return self._i

    @property
    def d(self) -> 'DecopReal':
        return self._d

    @property
    def i_cutoff(self) -> 'DecopReal':
        return self._i_cutoff

    @property
    def i_cutoff_enabled(self) -> 'DecopBoolean':
        return self._i_cutoff_enabled


class LocalOscillator07352890:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = DecopBoolean(client, name + ':enabled')
        self._attenuation_shg_raw = DecopInteger(client, name + ':attenuation-shg-raw')
        self._attenuation_fhg_raw = DecopInteger(client, name + ':attenuation-fhg-raw')
        self._phase_shift_shg = DecopReal(client, name + ':phase-shift-shg')
        self._phase_shift_fhg = DecopReal(client, name + ':phase-shift-fhg')

    @property
    def enabled(self) -> 'DecopBoolean':
        return self._enabled

    @property
    def attenuation_shg_raw(self) -> 'DecopInteger':
        return self._attenuation_shg_raw

    @property
    def attenuation_fhg_raw(self) -> 'DecopInteger':
        return self._attenuation_fhg_raw

    @property
    def phase_shift_shg(self) -> 'DecopReal':
        return self._phase_shift_shg

    @property
    def phase_shift_fhg(self) -> 'DecopReal':
        return self._phase_shift_fhg


class StatusParameters07352770:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._baseplate_temperature_limit = DecopReal(client, name + ':baseplate-temperature-limit')
        self._temperature_settle_time = DecopInteger(client, name + ':temperature-settle-time')
        self._pump_lock_settle_time = DecopInteger(client, name + ':pump-lock-settle-time')
        self._settle_down_delay = DecopInteger(client, name + ':settle-down-delay')
        self._power_margin_tolerance_time = DecopInteger(client, name + ':power-margin-tolerance-time')
        self._power_margin_threshold = DecopReal(client, name + ':power-margin-threshold')
        self._cavity_lock_settle_time = DecopInteger(client, name + ':cavity-lock-settle-time')
        self._cavity_lock_tolerance_factor = DecopInteger(client, name + ':cavity-lock-tolerance-factor')
        self._power_lock_settle_time = DecopInteger(client, name + ':power-lock-settle-time')
        self._cavity_scan_duration = DecopInteger(client, name + ':cavity-scan-duration')
        self._power_stabilization_strategy = DecopInteger(client, name + ':power-stabilization-strategy')
        self._power_stabilization_level_low_factor = DecopReal(client, name + ':power-stabilization-level-low-factor')
        self._power_output_relative_error_max = DecopReal(client, name + ':power-output-relative-error-max')
        self._power_output_relative_deviation_max = DecopReal(client, name + ':power-output-relative-deviation-max')
        self._operational_pump_power = DecopReal(client, name + ':operational-pump-power')
        self._degradation_detection_slope_threshold = DecopReal(client, name + ':degradation-detection-slope-threshold')
        self._degradation_detection_measurement_interval = DecopInteger(client, name + ':degradation-detection-measurement-interval')
        self._degradation_detection_number_of_measurements = DecopInteger(client, name + ':degradation-detection-number-of-measurements')

    @property
    def baseplate_temperature_limit(self) -> 'DecopReal':
        return self._baseplate_temperature_limit

    @property
    def temperature_settle_time(self) -> 'DecopInteger':
        return self._temperature_settle_time

    @property
    def pump_lock_settle_time(self) -> 'DecopInteger':
        return self._pump_lock_settle_time

    @property
    def settle_down_delay(self) -> 'DecopInteger':
        return self._settle_down_delay

    @property
    def power_margin_tolerance_time(self) -> 'DecopInteger':
        return self._power_margin_tolerance_time

    @property
    def power_margin_threshold(self) -> 'DecopReal':
        return self._power_margin_threshold

    @property
    def cavity_lock_settle_time(self) -> 'DecopInteger':
        return self._cavity_lock_settle_time

    @property
    def cavity_lock_tolerance_factor(self) -> 'DecopInteger':
        return self._cavity_lock_tolerance_factor

    @property
    def power_lock_settle_time(self) -> 'DecopInteger':
        return self._power_lock_settle_time

    @property
    def cavity_scan_duration(self) -> 'DecopInteger':
        return self._cavity_scan_duration

    @property
    def power_stabilization_strategy(self) -> 'DecopInteger':
        return self._power_stabilization_strategy

    @property
    def power_stabilization_level_low_factor(self) -> 'DecopReal':
        return self._power_stabilization_level_low_factor

    @property
    def power_output_relative_error_max(self) -> 'DecopReal':
        return self._power_output_relative_error_max

    @property
    def power_output_relative_deviation_max(self) -> 'DecopReal':
        return self._power_output_relative_deviation_max

    @property
    def operational_pump_power(self) -> 'DecopReal':
        return self._operational_pump_power

    @property
    def degradation_detection_slope_threshold(self) -> 'DecopReal':
        return self._degradation_detection_slope_threshold

    @property
    def degradation_detection_measurement_interval(self) -> 'DecopInteger':
        return self._degradation_detection_measurement_interval

    @property
    def degradation_detection_number_of_measurements(self) -> 'DecopInteger':
        return self._degradation_detection_number_of_measurements


class PdExt07352Bf0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._photodiode = DecopReal(client, name + ':photodiode')
        self._power = DecopReal(client, name + ':power')
        self._cal_offset = MutableDecopReal(client, name + ':cal-offset')
        self._cal_factor = MutableDecopReal(client, name + ':cal-factor')

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def photodiode(self) -> 'DecopReal':
        return self._photodiode

    @property
    def power(self) -> 'DecopReal':
        return self._power

    @property
    def cal_offset(self) -> 'MutableDecopReal':
        return self._cal_offset

    @property
    def cal_factor(self) -> 'MutableDecopReal':
        return self._cal_factor


class PowerStabilization07352D10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._gain = Gain07352Fb0(client, name + ':gain')
        self._sign = MutableDecopBoolean(client, name + ':sign')
        self._input_channel = MutableDecopInteger(client, name + ':input-channel')
        self._setpoint = MutableDecopReal(client, name + ':setpoint')
        self._window = Window07352C50(client, name + ':window')
        self._hold_output_on_unlock = MutableDecopBoolean(client, name + ':hold-output-on-unlock')
        self._output_channel = DecopInteger(client, name + ':output-channel')
        self._input_channel_value_act = DecopReal(client, name + ':input-channel-value-act')
        self._state = DecopInteger(client, name + ':state')
        self._feedforward_enabled = MutableDecopBoolean(client, name + ':feedforward-enabled')
        self._feedforward_factor = MutableDecopReal(client, name + ':feedforward-factor')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def gain(self) -> 'Gain07352Fb0':
        return self._gain

    @property
    def sign(self) -> 'MutableDecopBoolean':
        return self._sign

    @property
    def input_channel(self) -> 'MutableDecopInteger':
        return self._input_channel

    @property
    def setpoint(self) -> 'MutableDecopReal':
        return self._setpoint

    @property
    def window(self) -> 'Window07352C50':
        return self._window

    @property
    def hold_output_on_unlock(self) -> 'MutableDecopBoolean':
        return self._hold_output_on_unlock

    @property
    def output_channel(self) -> 'DecopInteger':
        return self._output_channel

    @property
    def input_channel_value_act(self) -> 'DecopReal':
        return self._input_channel_value_act

    @property
    def state(self) -> 'DecopInteger':
        return self._state

    @property
    def feedforward_enabled(self) -> 'MutableDecopBoolean':
        return self._feedforward_enabled

    @property
    def feedforward_factor(self) -> 'MutableDecopReal':
        return self._feedforward_factor


class Gain07352Fb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._all = MutableDecopReal(client, name + ':all')
        self._p = MutableDecopReal(client, name + ':p')
        self._i = MutableDecopReal(client, name + ':i')
        self._d = MutableDecopReal(client, name + ':d')

    @property
    def all(self) -> 'MutableDecopReal':
        return self._all

    @property
    def p(self) -> 'MutableDecopReal':
        return self._p

    @property
    def i(self) -> 'MutableDecopReal':
        return self._i

    @property
    def d(self) -> 'MutableDecopReal':
        return self._d


class Window07352C50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._enabled = MutableDecopBoolean(client, name + ':enabled')
        self._level_low = MutableDecopReal(client, name + ':level-low')
        self._level_hysteresis = MutableDecopReal(client, name + ':level-hysteresis')

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled

    @property
    def level_low(self) -> 'MutableDecopReal':
        return self._level_low

    @property
    def level_hysteresis(self) -> 'MutableDecopReal':
        return self._level_hysteresis


class Config07352E90:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._source = DecopString(client, name + ':source')
        self._product_name = DecopString(client, name + ':product-name')
        self._date = DecopString(client, name + ':date')
        self._caption = MutableDecopString(client, name + ':caption')
        self._pristine = DecopBoolean(client, name + ':pristine')

    @property
    def source(self) -> 'DecopString':
        return self._source

    @property
    def product_name(self) -> 'DecopString':
        return self._product_name

    @property
    def date(self) -> 'DecopString':
        return self._date

    @property
    def caption(self) -> 'MutableDecopString':
        return self._caption

    @property
    def pristine(self) -> 'DecopBoolean':
        return self._pristine

    def load(self) -> None:
        self.__client.exec(self.__name + ':load', input_stream=None, output_type=None, return_type=None)

    def save(self) -> None:
        self.__client.exec(self.__name + ':save', input_stream=None, output_type=None, return_type=None)

    def import_(self) -> None:
        self.__client.exec(self.__name + ':import', input_stream=None, output_type=None, return_type=None)

    def export(self) -> None:
        self.__client.exec(self.__name + ':export', input_stream=None, output_type=None, return_type=None)

    def retrieve(self) -> None:
        self.__client.exec(self.__name + ':retrieve', input_stream=None, output_type=None, return_type=None)

    def apply(self) -> None:
        self.__client.exec(self.__name + ':apply', input_stream=None, output_type=None, return_type=None)

    def show(self) -> None:
        self.__client.exec(self.__name + ':show', input_stream=None, output_type=None, return_type=None)

    def list(self) -> None:
        self.__client.exec(self.__name + ':list', input_stream=None, output_type=None, return_type=None)


class OpticalLock000Df1D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._id_ = DecopString(client, name + ':id')
        self._sample_rate = DecopReal(client, name + ':sample-rate')
        self._beat_level = DecopReal(client, name + ':beat-level')
        self._beat_spectrum = DecopBinary(client, name + ':beat-spectrum')
        self._beat_frequency_estimate = DecopReal(client, name + ':beat-frequency-estimate')
        self._beat_linewidth_estimate = DecopReal(client, name + ':beat-linewidth-estimate')
        self._beat_frequency = DecopReal(client, name + ':beat-frequency')
        self._beat_frequency_adev_1s = DecopReal(client, name + ':beat-frequency-adev-1s')
        self._tooth_index = DecopInteger(client, name + ':tooth-index')
        self._manual_tooth_index = MutableDecopInteger(client, name + ':manual-tooth-index')
        self._manual_tooth_index_enabled = MutableDecopBoolean(client, name + ':manual-tooth-index-enabled')
        self._beat_offset = MutableDecopInteger(client, name + ':beat-offset')
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._wavemeter_active = MutableDecopBoolean(client, name + ':wavemeter-active')
        self._coarse_frequency = DecopReal(client, name + ':coarse-frequency')
        self._coarse_wavelength = DecopReal(client, name + ':coarse-wavelength')
        self._monitoring_enabled = MutableDecopBoolean(client, name + ':monitoring-enabled')
        self._lock_status = DecopBoolean(client, name + ':lock-status')
        self._phase_frequency_detector = DecopString(client, name + ':phase-frequency-detector')

    @property
    def id_(self) -> 'DecopString':
        return self._id_

    @property
    def sample_rate(self) -> 'DecopReal':
        return self._sample_rate

    @property
    def beat_level(self) -> 'DecopReal':
        return self._beat_level

    @property
    def beat_spectrum(self) -> 'DecopBinary':
        return self._beat_spectrum

    @property
    def beat_frequency_estimate(self) -> 'DecopReal':
        return self._beat_frequency_estimate

    @property
    def beat_linewidth_estimate(self) -> 'DecopReal':
        return self._beat_linewidth_estimate

    @property
    def beat_frequency(self) -> 'DecopReal':
        return self._beat_frequency

    @property
    def beat_frequency_adev_1s(self) -> 'DecopReal':
        return self._beat_frequency_adev_1s

    @property
    def tooth_index(self) -> 'DecopInteger':
        return self._tooth_index

    @property
    def manual_tooth_index(self) -> 'MutableDecopInteger':
        return self._manual_tooth_index

    @property
    def manual_tooth_index_enabled(self) -> 'MutableDecopBoolean':
        return self._manual_tooth_index_enabled

    @property
    def beat_offset(self) -> 'MutableDecopInteger':
        return self._beat_offset

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def wavemeter_active(self) -> 'MutableDecopBoolean':
        return self._wavemeter_active

    @property
    def coarse_frequency(self) -> 'DecopReal':
        return self._coarse_frequency

    @property
    def coarse_wavelength(self) -> 'DecopReal':
        return self._coarse_wavelength

    @property
    def monitoring_enabled(self) -> 'MutableDecopBoolean':
        return self._monitoring_enabled

    @property
    def lock_status(self) -> 'DecopBoolean':
        return self._lock_status

    @property
    def phase_frequency_detector(self) -> 'DecopString':
        return self._phase_frequency_detector


class Laser1000Df6B0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._id_ = DecopString(client, name + ':id')
        self._sample_rate = DecopReal(client, name + ':sample-rate')
        self._beat_level = DecopReal(client, name + ':beat-level')
        self._beat_spectrum = DecopBinary(client, name + ':beat-spectrum')
        self._beat_frequency_estimate = DecopReal(client, name + ':beat-frequency-estimate')
        self._beat_linewidth_estimate = DecopReal(client, name + ':beat-linewidth-estimate')
        self._integrator_enabled = MutableDecopBoolean(client, name + ':integrator-enabled')
        self._piezo_voltage = MutableDecopReal(client, name + ':piezo-voltage')
        self._beat_frequency = DecopReal(client, name + ':beat-frequency')
        self._beat_frequency_adev_1s = DecopReal(client, name + ':beat-frequency-adev-1s')
        self._tooth_index = DecopInteger(client, name + ':tooth-index')
        self._manual_tooth_index = MutableDecopInteger(client, name + ':manual-tooth-index')
        self._manual_tooth_index_enabled = MutableDecopBoolean(client, name + ':manual-tooth-index-enabled')
        self._beat_offset = MutableDecopInteger(client, name + ':beat-offset')
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._wavemeter_active = MutableDecopBoolean(client, name + ':wavemeter-active')
        self._coarse_frequency = DecopReal(client, name + ':coarse-frequency')
        self._coarse_wavelength = DecopReal(client, name + ':coarse-wavelength')
        self._monitoring_enabled = MutableDecopBoolean(client, name + ':monitoring-enabled')
        self._lock_status = DecopBoolean(client, name + ':lock-status')
        self._phase_frequency_detector = DecopString(client, name + ':phase-frequency-detector')

    @property
    def id_(self) -> 'DecopString':
        return self._id_

    @property
    def sample_rate(self) -> 'DecopReal':
        return self._sample_rate

    @property
    def beat_level(self) -> 'DecopReal':
        return self._beat_level

    @property
    def beat_spectrum(self) -> 'DecopBinary':
        return self._beat_spectrum

    @property
    def beat_frequency_estimate(self) -> 'DecopReal':
        return self._beat_frequency_estimate

    @property
    def beat_linewidth_estimate(self) -> 'DecopReal':
        return self._beat_linewidth_estimate

    @property
    def integrator_enabled(self) -> 'MutableDecopBoolean':
        return self._integrator_enabled

    @property
    def piezo_voltage(self) -> 'MutableDecopReal':
        return self._piezo_voltage

    @property
    def beat_frequency(self) -> 'DecopReal':
        return self._beat_frequency

    @property
    def beat_frequency_adev_1s(self) -> 'DecopReal':
        return self._beat_frequency_adev_1s

    @property
    def tooth_index(self) -> 'DecopInteger':
        return self._tooth_index

    @property
    def manual_tooth_index(self) -> 'MutableDecopInteger':
        return self._manual_tooth_index

    @property
    def manual_tooth_index_enabled(self) -> 'MutableDecopBoolean':
        return self._manual_tooth_index_enabled

    @property
    def beat_offset(self) -> 'MutableDecopInteger':
        return self._beat_offset

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def wavemeter_active(self) -> 'MutableDecopBoolean':
        return self._wavemeter_active

    @property
    def coarse_frequency(self) -> 'DecopReal':
        return self._coarse_frequency

    @property
    def coarse_wavelength(self) -> 'DecopReal':
        return self._coarse_wavelength

    @property
    def monitoring_enabled(self) -> 'MutableDecopBoolean':
        return self._monitoring_enabled

    @property
    def lock_status(self) -> 'DecopBoolean':
        return self._lock_status

    @property
    def phase_frequency_detector(self) -> 'DecopString':
        return self._phase_frequency_detector


class LaserCommon0011Cab0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._repetition_rate = DecopReal(client, name + ':repetition-rate')
        self._repetition_rate_phase_error = DecopReal(client, name + ':repetition-rate-phase-error')
        self._repetition_rate_status = DecopBoolean(client, name + ':repetition-rate-status')

    @property
    def repetition_rate(self) -> 'DecopReal':
        return self._repetition_rate

    @property
    def repetition_rate_phase_error(self) -> 'DecopReal':
        return self._repetition_rate_phase_error

    @property
    def repetition_rate_status(self) -> 'DecopBoolean':
        return self._repetition_rate_status


class Monitoring0011Cb10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._logs = DecopString(client, name + ':logs')
        self._running = DecopBoolean(client, name + ':running')
        self._remaining_time = DecopReal(client, name + ':remaining-time')
        self._log_name = MutableDecopString(client, name + ':log-name')

    @property
    def logs(self) -> 'DecopString':
        return self._logs

    @property
    def running(self) -> 'DecopBoolean':
        return self._running

    @property
    def remaining_time(self) -> 'DecopReal':
        return self._remaining_time

    @property
    def log_name(self) -> 'MutableDecopString':
        return self._log_name

    def start(self) -> None:
        self.__client.exec(self.__name + ':start', input_stream=None, output_type=None, return_type=None)

    def stop(self) -> None:
        self.__client.exec(self.__name + ':stop', input_stream=None, output_type=None, return_type=None)


class PhaseFrequencyDetector000E43A4:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._PFD1 = Pfd1000Df830(client, name + ':PFD1')
        self._PFD2 = Pfd20012Fef0(client, name + ':PFD2')

    @property
    def PFD1(self) -> 'Pfd1000Df830':
        return self._PFD1

    @property
    def PFD2(self) -> 'Pfd20012Fef0':
        return self._PFD2


class Pfd1000Df830:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._device_type = DecopString(client, name + ':device-type')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._firmware_revision = DecopString(client, name + ':firmware-revision')
        self._auxiliary_output = MutableDecopInteger(client, name + ':auxiliary-output')
        self._auxiliary_output_txt = DecopString(client, name + ':auxiliary-output-txt')
        self._monitor_signal = MutableDecopInteger(client, name + ':monitor-signal')
        self._monitor_signal_txt = DecopString(client, name + ':monitor-signal-txt')
        self._main_out_gain = MutableDecopInteger(client, name + ':main-out-gain')
        self._main_out_enabled = MutableDecopBoolean(client, name + ':main-out-enabled')
        self._rf_divider = MutableDecopInteger(client, name + ':rf-divider')
        self._rf_filter_frequency = MutableDecopReal(client, name + ':rf-filter-frequency')
        self._rf_gain_act = DecopReal(client, name + ':rf-gain-act')
        self._rf_gain_set = MutableDecopReal(client, name + ':rf-gain-set')
        self._rf_agc_enabled = MutableDecopBoolean(client, name + ':rf-agc-enabled')
        self._rf_agc_target_level = MutableDecopReal(client, name + ':rf-agc-target-level')
        self._phase_error_inverted = MutableDecopBoolean(client, name + ':phase-error-inverted')
        self._rf_level = DecopReal(client, name + ':rf-level')
        self._rf_frequency = DecopReal(client, name + ':rf-frequency')
        self._ext_ref_frequency = DecopReal(client, name + ':ext-ref-frequency')
        self._ext_ref_detected = DecopBoolean(client, name + ':ext-ref-detected')
        self._cycle_slip_detected = DecopBoolean(client, name + ':cycle-slip-detected')
        self._common_status = DecopInteger(client, name + ':common-status')
        self._common_status_txt = DecopString(client, name + ':common-status-txt')
        self._common_error = DecopInteger(client, name + ':common-error')
        self._common_error_txt = DecopString(client, name + ':common-error-txt')
        self._pfd_error = DecopInteger(client, name + ':pfd-error')
        self._pfd_error_txt = DecopString(client, name + ':pfd-error-txt')

    @property
    def device_type(self) -> 'DecopString':
        return self._device_type

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def firmware_revision(self) -> 'DecopString':
        return self._firmware_revision

    @property
    def auxiliary_output(self) -> 'MutableDecopInteger':
        return self._auxiliary_output

    @property
    def auxiliary_output_txt(self) -> 'DecopString':
        return self._auxiliary_output_txt

    @property
    def monitor_signal(self) -> 'MutableDecopInteger':
        return self._monitor_signal

    @property
    def monitor_signal_txt(self) -> 'DecopString':
        return self._monitor_signal_txt

    @property
    def main_out_gain(self) -> 'MutableDecopInteger':
        return self._main_out_gain

    @property
    def main_out_enabled(self) -> 'MutableDecopBoolean':
        return self._main_out_enabled

    @property
    def rf_divider(self) -> 'MutableDecopInteger':
        return self._rf_divider

    @property
    def rf_filter_frequency(self) -> 'MutableDecopReal':
        return self._rf_filter_frequency

    @property
    def rf_gain_act(self) -> 'DecopReal':
        return self._rf_gain_act

    @property
    def rf_gain_set(self) -> 'MutableDecopReal':
        return self._rf_gain_set

    @property
    def rf_agc_enabled(self) -> 'MutableDecopBoolean':
        return self._rf_agc_enabled

    @property
    def rf_agc_target_level(self) -> 'MutableDecopReal':
        return self._rf_agc_target_level

    @property
    def phase_error_inverted(self) -> 'MutableDecopBoolean':
        return self._phase_error_inverted

    @property
    def rf_level(self) -> 'DecopReal':
        return self._rf_level

    @property
    def rf_frequency(self) -> 'DecopReal':
        return self._rf_frequency

    @property
    def ext_ref_frequency(self) -> 'DecopReal':
        return self._ext_ref_frequency

    @property
    def ext_ref_detected(self) -> 'DecopBoolean':
        return self._ext_ref_detected

    @property
    def cycle_slip_detected(self) -> 'DecopBoolean':
        return self._cycle_slip_detected

    @property
    def common_status(self) -> 'DecopInteger':
        return self._common_status

    @property
    def common_status_txt(self) -> 'DecopString':
        return self._common_status_txt

    @property
    def common_error(self) -> 'DecopInteger':
        return self._common_error

    @property
    def common_error_txt(self) -> 'DecopString':
        return self._common_error_txt

    @property
    def pfd_error(self) -> 'DecopInteger':
        return self._pfd_error

    @property
    def pfd_error_txt(self) -> 'DecopString':
        return self._pfd_error_txt

    def cycle_slip_reset(self) -> None:
        self.__client.exec(self.__name + ':cycle-slip-reset', input_stream=None, output_type=None, return_type=None)

    def settings_reset(self) -> None:
        self.__client.exec(self.__name + ':settings-reset', input_stream=None, output_type=None, return_type=None)

    def settings_save(self) -> None:
        self.__client.exec(self.__name + ':settings-save', input_stream=None, output_type=None, return_type=None)

    def common_reset(self) -> None:
        self.__client.exec(self.__name + ':common-reset', input_stream=None, output_type=None, return_type=None)

    def pfd_reset(self) -> None:
        self.__client.exec(self.__name + ':pfd-reset', input_stream=None, output_type=None, return_type=None)


class Pfd20012Fef0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._device_type = DecopString(client, name + ':device-type')
        self._serial_number = DecopString(client, name + ':serial-number')
        self._firmware_revision = DecopString(client, name + ':firmware-revision')
        self._auxiliary_output = MutableDecopInteger(client, name + ':auxiliary-output')
        self._auxiliary_output_txt = DecopString(client, name + ':auxiliary-output-txt')
        self._monitor_signal = MutableDecopInteger(client, name + ':monitor-signal')
        self._monitor_signal_txt = DecopString(client, name + ':monitor-signal-txt')
        self._main_out_gain = MutableDecopInteger(client, name + ':main-out-gain')
        self._main_out_enabled = MutableDecopBoolean(client, name + ':main-out-enabled')
        self._rf_divider = MutableDecopInteger(client, name + ':rf-divider')
        self._rf_filter_frequency = MutableDecopReal(client, name + ':rf-filter-frequency')
        self._rf_gain_act = DecopReal(client, name + ':rf-gain-act')
        self._rf_gain_set = MutableDecopReal(client, name + ':rf-gain-set')
        self._rf_agc_enabled = MutableDecopBoolean(client, name + ':rf-agc-enabled')
        self._rf_agc_target_level = MutableDecopReal(client, name + ':rf-agc-target-level')
        self._phase_error_inverted = MutableDecopBoolean(client, name + ':phase-error-inverted')
        self._rf_level = DecopReal(client, name + ':rf-level')
        self._rf_frequency = DecopReal(client, name + ':rf-frequency')
        self._ext_ref_frequency = DecopReal(client, name + ':ext-ref-frequency')
        self._ext_ref_detected = DecopBoolean(client, name + ':ext-ref-detected')
        self._cycle_slip_detected = DecopBoolean(client, name + ':cycle-slip-detected')
        self._common_status = DecopInteger(client, name + ':common-status')
        self._common_status_txt = DecopString(client, name + ':common-status-txt')
        self._common_error = DecopInteger(client, name + ':common-error')
        self._common_error_txt = DecopString(client, name + ':common-error-txt')
        self._pfd_error = DecopInteger(client, name + ':pfd-error')
        self._pfd_error_txt = DecopString(client, name + ':pfd-error-txt')

    @property
    def device_type(self) -> 'DecopString':
        return self._device_type

    @property
    def serial_number(self) -> 'DecopString':
        return self._serial_number

    @property
    def firmware_revision(self) -> 'DecopString':
        return self._firmware_revision

    @property
    def auxiliary_output(self) -> 'MutableDecopInteger':
        return self._auxiliary_output

    @property
    def auxiliary_output_txt(self) -> 'DecopString':
        return self._auxiliary_output_txt

    @property
    def monitor_signal(self) -> 'MutableDecopInteger':
        return self._monitor_signal

    @property
    def monitor_signal_txt(self) -> 'DecopString':
        return self._monitor_signal_txt

    @property
    def main_out_gain(self) -> 'MutableDecopInteger':
        return self._main_out_gain

    @property
    def main_out_enabled(self) -> 'MutableDecopBoolean':
        return self._main_out_enabled

    @property
    def rf_divider(self) -> 'MutableDecopInteger':
        return self._rf_divider

    @property
    def rf_filter_frequency(self) -> 'MutableDecopReal':
        return self._rf_filter_frequency

    @property
    def rf_gain_act(self) -> 'DecopReal':
        return self._rf_gain_act

    @property
    def rf_gain_set(self) -> 'MutableDecopReal':
        return self._rf_gain_set

    @property
    def rf_agc_enabled(self) -> 'MutableDecopBoolean':
        return self._rf_agc_enabled

    @property
    def rf_agc_target_level(self) -> 'MutableDecopReal':
        return self._rf_agc_target_level

    @property
    def phase_error_inverted(self) -> 'MutableDecopBoolean':
        return self._phase_error_inverted

    @property
    def rf_level(self) -> 'DecopReal':
        return self._rf_level

    @property
    def rf_frequency(self) -> 'DecopReal':
        return self._rf_frequency

    @property
    def ext_ref_frequency(self) -> 'DecopReal':
        return self._ext_ref_frequency

    @property
    def ext_ref_detected(self) -> 'DecopBoolean':
        return self._ext_ref_detected

    @property
    def cycle_slip_detected(self) -> 'DecopBoolean':
        return self._cycle_slip_detected

    @property
    def common_status(self) -> 'DecopInteger':
        return self._common_status

    @property
    def common_status_txt(self) -> 'DecopString':
        return self._common_status_txt

    @property
    def common_error(self) -> 'DecopInteger':
        return self._common_error

    @property
    def common_error_txt(self) -> 'DecopString':
        return self._common_error_txt

    @property
    def pfd_error(self) -> 'DecopInteger':
        return self._pfd_error

    @property
    def pfd_error_txt(self) -> 'DecopString':
        return self._pfd_error_txt

    def cycle_slip_reset(self) -> None:
        self.__client.exec(self.__name + ':cycle-slip-reset', input_stream=None, output_type=None, return_type=None)

    def settings_reset(self) -> None:
        self.__client.exec(self.__name + ':settings-reset', input_stream=None, output_type=None, return_type=None)

    def settings_save(self) -> None:
        self.__client.exec(self.__name + ':settings-save', input_stream=None, output_type=None, return_type=None)

    def common_reset(self) -> None:
        self.__client.exec(self.__name + ':common-reset', input_stream=None, output_type=None, return_type=None)

    def pfd_reset(self) -> None:
        self.__client.exec(self.__name + ':pfd-reset', input_stream=None, output_type=None, return_type=None)


class Wavemeter0012Fa10:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._channel1 = Channel10012Fc50(client, name + ':channel1')
        self._channel2 = Channel20012Fa70(client, name + ':channel2')
        self._channel3 = Channel30012F890(client, name + ':channel3')
        self._channel4 = Channel40012Fcb0(client, name + ':channel4')
        self._channel5 = Channel5001301F0(client, name + ':channel5')
        self._channel6 = Channel60012F7D0(client, name + ':channel6')
        self._channel7 = Channel7001300D0(client, name + ':channel7')
        self._channel8 = Channel80012Fb30(client, name + ':channel8')

    @property
    def channel1(self) -> 'Channel10012Fc50':
        return self._channel1

    @property
    def channel2(self) -> 'Channel20012Fa70':
        return self._channel2

    @property
    def channel3(self) -> 'Channel30012F890':
        return self._channel3

    @property
    def channel4(self) -> 'Channel40012Fcb0':
        return self._channel4

    @property
    def channel5(self) -> 'Channel5001301F0':
        return self._channel5

    @property
    def channel6(self) -> 'Channel60012F7D0':
        return self._channel6

    @property
    def channel7(self) -> 'Channel7001300D0':
        return self._channel7

    @property
    def channel8(self) -> 'Channel80012Fb30':
        return self._channel8


class Channel10012Fc50:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel20012Fa70:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel30012F890:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel40012Fcb0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel5001301F0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel60012F7D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel7001300D0:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Channel80012Fb30:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._frequency = DecopReal(client, name + ':frequency')
        self._wavelength = DecopReal(client, name + ':wavelength')
        self._enabled = MutableDecopBoolean(client, name + ':enabled')

    @property
    def frequency(self) -> 'DecopReal':
        return self._frequency

    @property
    def wavelength(self) -> 'DecopReal':
        return self._wavelength

    @property
    def enabled(self) -> 'MutableDecopBoolean':
        return self._enabled


class Components0013A174:
    def __init__(self, client: Client, name: str) -> None:
        self.__client = client
        self.__name = name
        self._adc_state_id = DecopInteger(client, name + ':adc-state-id')
        self._adc_state_txt = DecopString(client, name + ':adc-state-txt')
        self._dfc_core_state_id = DecopInteger(client, name + ':dfc-core-state-id')
        self._dfc_core_state_txt = DecopString(client, name + ':dfc-core-state-txt')
        self._dlcpro_state_id = DecopInteger(client, name + ':dlcpro-state-id')
        self._dlcpro_state_txt = DecopString(client, name + ':dlcpro-state-txt')
        self._freq_meter_state_id = DecopInteger(client, name + ':freq-meter-state-id')
        self._freq_meter_state_txt = DecopString(client, name + ':freq-meter-state-txt')
        self._pfd_1_state_id = DecopInteger(client, name + ':pfd-1-state-id')
        self._pfd_1_state_txt = DecopString(client, name + ':pfd-1-state-txt')
        self._pfd_2_state_id = DecopInteger(client, name + ':pfd-2-state-id')
        self._pfd_2_state_txt = DecopString(client, name + ':pfd-2-state-txt')
        self._wavemeter_state_id = DecopInteger(client, name + ':wavemeter-state-id')
        self._wavemeter_state_txt = DecopString(client, name + ':wavemeter-state-txt')

    @property
    def adc_state_id(self) -> 'DecopInteger':
        return self._adc_state_id

    @property
    def adc_state_txt(self) -> 'DecopString':
        return self._adc_state_txt

    @property
    def dfc_core_state_id(self) -> 'DecopInteger':
        return self._dfc_core_state_id

    @property
    def dfc_core_state_txt(self) -> 'DecopString':
        return self._dfc_core_state_txt

    @property
    def dlcpro_state_id(self) -> 'DecopInteger':
        return self._dlcpro_state_id

    @property
    def dlcpro_state_txt(self) -> 'DecopString':
        return self._dlcpro_state_txt

    @property
    def freq_meter_state_id(self) -> 'DecopInteger':
        return self._freq_meter_state_id

    @property
    def freq_meter_state_txt(self) -> 'DecopString':
        return self._freq_meter_state_txt

    @property
    def pfd_1_state_id(self) -> 'DecopInteger':
        return self._pfd_1_state_id

    @property
    def pfd_1_state_txt(self) -> 'DecopString':
        return self._pfd_1_state_txt

    @property
    def pfd_2_state_id(self) -> 'DecopInteger':
        return self._pfd_2_state_id

    @property
    def pfd_2_state_txt(self) -> 'DecopString':
        return self._pfd_2_state_txt

    @property
    def wavemeter_state_id(self) -> 'DecopInteger':
        return self._wavemeter_state_id

    @property
    def wavemeter_state_txt(self) -> 'DecopString':
        return self._wavemeter_state_txt


class DFCCS:
    def __init__(self, connection: Connection) -> None:
        self.__client = Client(connection)
        self._ul = DecopInteger(self.__client, 'ul')
        self._system_type = DecopString(self.__client, 'system-type')
        self._system_label = DecopString(self.__client, 'system-label')
        self._fw_ver = DecopString(self.__client, 'fw-ver')
        self._tree_id = DecopString(self.__client, 'tree-id')
        self._dfc_core = DfcCore0011B894(self.__client, 'dfc-core')
        self._dlcpro = Dlcpro000Daf74(self.__client, 'dlcpro')
        self._optical_lock = OpticalLock000Df1D0(self.__client, 'optical-lock')
        self._laser_1 = Laser1000Df6B0(self.__client, 'laser-1')
        self._laser_common = LaserCommon0011Cab0(self.__client, 'laser-common')
        self._monitoring = Monitoring0011Cb10(self.__client, 'monitoring')
        self._phase_frequency_detector = PhaseFrequencyDetector000E43A4(self.__client, 'phase-frequency-detector')
        self._wavemeter = Wavemeter0012Fa10(self.__client, 'wavemeter')
        self._components = Components0013A174(self.__client, 'components')
        self._state_id = DecopInteger(self.__client, 'state-id')
        self._state_txt = DecopString(self.__client, 'state-txt')

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def open(self) -> None:
        self.__client.open()

    def close(self) -> None:
        self.__client.close()

    def run(self, timeout: int = None) -> None:
        self.__client.run(timeout)

    def stop(self) -> None:
        self.__client.stop()

    def poll(self) -> None:
        self.__client.poll()

    @property
    def ul(self) -> 'DecopInteger':
        return self._ul

    @property
    def system_type(self) -> 'DecopString':
        return self._system_type

    @property
    def system_label(self) -> 'DecopString':
        return self._system_label

    @property
    def fw_ver(self) -> 'DecopString':
        return self._fw_ver

    @property
    def tree_id(self) -> 'DecopString':
        return self._tree_id

    @property
    def dfc_core(self) -> 'DfcCore0011B894':
        return self._dfc_core

    @property
    def dlcpro(self) -> 'Dlcpro000Daf74':
        return self._dlcpro

    @property
    def optical_lock(self) -> 'OpticalLock000Df1D0':
        return self._optical_lock

    @property
    def laser_1(self) -> 'Laser1000Df6B0':
        return self._laser_1

    @property
    def laser_common(self) -> 'LaserCommon0011Cab0':
        return self._laser_common

    @property
    def monitoring(self) -> 'Monitoring0011Cb10':
        return self._monitoring

    @property
    def phase_frequency_detector(self) -> 'PhaseFrequencyDetector000E43A4':
        return self._phase_frequency_detector

    @property
    def wavemeter(self) -> 'Wavemeter0012Fa10':
        return self._wavemeter

    @property
    def components(self) -> 'Components0013A174':
        return self._components

    @property
    def state_id(self) -> 'DecopInteger':
        return self._state_id

    @property
    def state_txt(self) -> 'DecopString':
        return self._state_txt

    def change_ul(self, ul: UserLevel, passwd: str) -> int:
        assert isinstance(ul, UserLevel), "expected type 'UserLevel' for parameter 'ul', got '{}'".format(type(ul))
        assert isinstance(passwd, str), "expected type 'str' for parameter 'passwd', got '{}'".format(type(passwd))
        return self.__client.change_ul(ul, passwd)

    def state_reset(self) -> None:
        self.__client.exec('state-reset', input_stream=None, output_type=None, return_type=None)

