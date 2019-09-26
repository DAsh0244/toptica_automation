from serial import (
    serial_for_url as _serial_for_url, 
    Serial as _Serial
) 
from  serial.tools.list_ports import comports as _comports
from utils import logger
from atexit import ( register as _register, unregister as _unregister )

class ThorlabsShutter:
    def __init__(self, addr,timeout=1.0):
        if isinstance(addr,_Serial):
            self._conn = addr
        else:
            self._conn = _serial_for_url(url=addr,timeout=timeout)
        _register(self.close)
        self._conn.write(b"0in")
        resp = self._conn.readline().decode('utf-8').strip()
        self._serial_num = resp[5:13] 
        self.home()
        self.open = True

    @classmethod
    def from_serial_num(cls,serial_num:str):
        for port,_,_ in _comports():
            try:
                s = _serial_for_url(port,timeout=1.0)
                s.write(b'0in')
                if serial_num in s.readline().decode('utf-8'):
                    return cls(s)
            except Exception:
                pass
        else:
            logger.error('Device not found!')

    def home(self):
        self._conn.write(b'0ho0')
    
    def forward(self):
        self._conn.write(b'0fw')

    def open_shutter(self):
        self.home()
        self.open=True

    def close_shutter(self):
        self.forward()
        self.open=False
    
    def toggle_shutter(self):
        if self.open:
            self.close_shutter()
        else:
            self.open_shutter()

    def close(self):
        self._conn.close()
     
    def __del__(self):
        try:
            self.close()
        except Exception as e:
            print(e)
        _unregister(self.close)
