#orig
# from libs import dlpromotor
from serial import Serial as _Serial
import socket
from heapq import nsmallest
from atexit import ( register as _register, unregister as _unregister )
import itertools
import operator
from enum import Enum
from collections import namedtuple 

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



Point = namedtuple('Point','direction position wavelength frequency')
_Reply = namedtuple('Reply','reply_address module_addr status command_num value checksum')

class Reply(_Reply):
    @classmethod
    def from_raw_bytes(cls, raw_bytes:bytes):
        addr,module,status,comnum = raw_bytes[0:4]
        value = int.from_bytes(raw_bytes[4:8], byteorder='big', signed=False)
        checksum=raw_bytes[8]
        return cls(addr,module,status,comnum,value,checksum)

NO_REPLY = Reply(0,0,0,0,0,0)

class DLMotorStatus(Enum):
    SUCCESS = 100
    LOADED = 101
    WRONG_CHECKSUM = 1
    INVALID_CMD = 2
    WRONG_TYPE = 3
    INVALID_VALUE = 4
    EEPROM_LOCKED = 5 
    NOT_AVAIBLE = 6

class DLMotor:

    CMDS = {
        'ROR':   1,
        'ROL':   2,
        'MST':   3,
        'MVP':   4,
        'SAP':   5,
        'GAP':   6,
        'STAP':  7,
        'RSAP':  8,
        'SGP':   9,
        'GGP':  10,
        'STGP': 11,
        'RSGP': 12,
        'RFS':  13,
        'SIO':  14,
        'GIO':  15,
        'SCO':  30,
        'GCO':  31,
        'CCO':  32,
        '138': 138,
    }
    
    
    # position,
    HYSTERESIS_CURVE = 'default_hysteris_curve_10_26_2019.csv'
    
    def __init__(self,port:str,timeout:float=1.0,offset_wavelength:float=0,offset_frequency:float=0,motor:int=2,home:bool=True,hysteresis_curve=None,enforce_limits:bool=True):
    # def __init__(self,port:str,timeout:float=1.0,motor:int=2,home:bool=True,hysteresis_curve=None,enforce_limits:bool=True,wavemeter_addr=None):
        self._port = _Serial(port=port,timeout=timeout)
        self.saved_positions = []
        self._direction = None
        self._address = 1
        self._motor = 2
        self.wavelength_offset = offset_wavelength
        self.frequency_offset = offset_frequency
        self.enforce_limits = enforce_limits
        # self.wavemeter_addr = socket.create_connection((wavemeter_addr,1998),timeout=1.0)
        if hysteresis_curve is None:
            self._hysteresis_curve = self._load_hysteresis_curve(self.HYSTERESIS_CURVE,header=True)
        else:
            self._hysteresis_curve = self._load_hysteresis_curve(hysteresis_curve)
        self._pos_max = max(max(self._hysteresis_curve['up']),max(self._hysteresis_curve['down'])).position
        self._pos_min = min(min(self._hysteresis_curve['up']),min(self._hysteresis_curve['down'])).position
        if home:
            self.home_motor()
            self.cycle_position('down')
            self.cycle_position('up')
            self.cycle_position('down')
            self.cycle_position('up')
        _register(self.close)

    def close(self):
        self._port.close()
        _unregister(self.close)

    # def __del__(self):
    #     try:
    #         self.close()
    #     except Exception as e:
    #         print(e)
    #     _unregister(self.close)

    def _load_hysteresis_curve(self,curve_data_file:str,header:bool=True):
        """
        loads hysteresis curve data for lookup purposes
        
        Arguments:
            curve_data_file {str} -- [filename to read - must be csv structure of {direction},{position},{wavelength(nm)},{frequency(THz)}]
        
        Keyword Arguments:
            header {bool} -- [whether the file has a header row or not. skips first row if true.] (default: {True})
        """
        with open(curve_data_file,'r') as data:
            up_curve = []
            down_curve = []
            if header:
                next(data)
            for row in data:
                direction,pos,wave,freq = row.strip().split(',')
                point = Point(direction,int(pos),float(wave),float(freq))
                if point.direction == 'up':
                    up_curve.append(point)
                elif point.direction == 'down':
                    down_curve.append(point)
                else:
                    raise ValueError('Incorrect format detected')
        return {'up':sorted(up_curve,key=operator.itemgetter(1)),'down':sorted(down_curve,key=operator.itemgetter(1))}

    @property
    def direction(self):
        return self._direction

    @property
    def pos_max(self):
        return self._pos_max
    
    @property
    def pos_min(self):
        return self._pos_min

    def wait_for_movement(self,timeout=5):
        self.send_cmd('138',0,0b100)
        res = self.read_response()
        t = 0
        while res.status != 128 and t < timeout:
            res=self.read_response()
            t += 1
        if t == timeout:
            return -1
        else:
            return 0

    def home_motor(self):
        self.send_cmd('MVP',0,0)
        self.wait_for_movement()
        self.send_cmd('MVP',0,self.pos_min)
        self._direction = 'up'
        self.wait_for_movement()

    def send_cmd(self,command,cmd_type,value):
        Tx = {}
        if value < 0:
            """ checks for negative numbers
        and converts them to appropriate value for
        the Trinamic control"""
            value += 4294967296
        Tx[0] = (self._address)
        Tx[1] = (self.CMDS[command])
        Tx[2] = (cmd_type)
        Tx[3] = (self._motor)
        hex_value = ('%08x' % value)
        #print("Hex value:", hex_value,"\n")
        Tx[4] = int(hex_value[0:2],16)
        Tx[5] = int(hex_value[2:4],16)
        Tx[6] = int(hex_value[4:6],16)
        Tx[7] = int(hex_value[6:],16)
        Tx[8] = 0
        i = 0
        cmd_array = []
        while i < 8:
            Tx[8] += Tx[i]
            cmd_array.append(Tx[i])
            #print('byte',i,'int',Tx[i],' Checksum:',Tx[8])
            i += 1
        Tx[8] = ("%08x" % Tx[8])
        #print('raw hex checksum:',Tx[8])
        Tx[8] = int(Tx[8][-2:],16)
        cmd_array.append(Tx[8])
        #print('hex checksum parsed int',Tx[8])    
        cmd_bytes = bytearray(cmd_array)
        #print(cmd_bytes)
        self._port.write(cmd_bytes)
    
    def read_response(self):
        resp = self._port.read(9)
        if len(resp) < 9:
            return NO_REPLY
        else:
            return Reply.from_raw_bytes(resp)

    @property
    def position(self):
        # fill in send cmd command structure
        self.send_cmd('GAP',1,0)
        resp = self.read_response()
        return resp.value 

    @position.setter
    def position(self,position:int):
        if self.enforce_limits:
            position = min(max(position,self._pos_min),self._pos_max)
        if self.position < position:
            self._direction = 'up'
        elif self.position > position:
            self._direction = 'down'
        self.send_cmd('MVP',0,position)

    def cycle_position(self,curve):
        """
        moves to the starting point of the desired curve
        
        Arguments:
            curve {str} -- ['up' or 'down' - desired curve to end up on]
        """
        if curve == 'up':
            self.position = self._pos_max
            self.wait_for_movement(timeout=1)
            self.position = self._pos_min
            self.wait_for_movement()
            self._direction = 'up'
        elif curve == 'down':
            self.position = self._pos_min
            self.wait_for_movement(timeout=1)
            self.position = self._pos_max
            self.wait_for_movement()
            self._direction = 'down'

    # @property
    # def target_wavelength(self):
    #     return self._hysteresis_curve[self._direction]

    # @property
    # def wavelength(self):
    #     self.wavemeter_addr.send(b'(param-ref \'wavemeter:channel1:wavelength)')
    #     return float(self.wavemeter_addr.recv(1024).decode('utf-8')[:-2])

    @staticmethod
    def _interpolate(x1,y1,x0,y0,x):
        # if (x <= x0) {return y0;}
        # if (x >= x1) {return y1;}
        t = x-x0
        t /= (x1-x0)
        return y0 + t*(y1-y0)        

    def set_wavelength(self,wavelength:float):
        """
        implements a lookup between position and wavelength on the loaded hysteresis curve
        
        Arguments:
            wavelength {float} -- [desired wavelength to move to - will be accurate to ~0.2nm]
        """
        # find closest points to wavelength - w1 < w2
        p1,p2 = nsmallest(2, self._hysteresis_curve[self._direction], key=lambda x: abs(x.wavelength-(wavelength+self.wavelength_offset)))
        pos = self._interpolate(p1.wavelength,p1.position,p2.wavelength,p2.position,(wavelength+self.wavelength_offset))
        logger.debug('wavelength: %f, target_pos: %d, direction:%s, p1: %s, p2: %s',wavelength,pos,self.direction,repr(p1),repr(p2))
        if pos > self.position and self.direction == 'down':
            self.cycle_position('up')
            self.cycle_position('down')
        elif pos < self.position and self.direction == 'up':
            self.cycle_position('down')
            self.cycle_position('up')
        self.position = int(round(pos))

    def set_frequency(self,frequency:float):
        """
        implements a lookup between position and frequency on the loaded hysteresis curve
        
        Arguments:
            wavelength {float} -- [desired frequency (THz) to go to - will be accurate to ~ ___ THz]
        """
        # find closest points to wavelength - w1 < w2
        p1,p2 = nsmallest(2, self._hysteresis_curve[self._direction], key=lambda x: abs(x.frequency-(frequency+self.frequency_offset)))
        pos = self._interpolate(p1.frequency,p1.position,p2.frequency,p2.position,(frequency+self.frequency_offset))
        logger.debug('frequency: %f, target_pos: %d, direction:%s, p1: %s, p2: %s',frequency,pos,self.direction,repr(p1),repr(p2))
        if pos > self.position and self.direction == 'down':
            self.cycle_position('up')
            self.cycle_position('down')
        elif pos < self.position and self.direction == 'up':
            self.cycle_position('down')
            self.cycle_position('up')
        self.position = int(round(pos))

