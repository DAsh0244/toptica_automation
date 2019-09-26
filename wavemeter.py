# implements wavemeter functionality,
# contains possiblity of interfacing wavemeter via
#   1. DFCServer
#   2. direct com-port and DLL -- NOT IMPLEMENTED YET

# from serial import Serial as _Serial
import socket as _socket
from time import sleep as _sleep
from atexit import ( register as _register, unregister as _unregister )

class WavemeterDFC:
    def __init__(self,host,port=1998,timeout=0.01):
        self._host = host
        self._port = port
        self._conn = _socket.create_connection((self._host,self._port),timeout=timeout)
        self.sleep_time = 0.01
        _sleep(self.sleep_time)
        self._conn.recv(1024)
        _register(self.close)
    def measure_wavelength(self):
        self.clear_buffer()
        self._conn.send(b"(param-ref 'wavemeter:channel1:wavelength)\n")
        _sleep(self.sleep_time)
        return float(self._conn.recv(1024).decode('utf-8')[:-2])
    def measure_frequency(self):
        self.clear_buffer()
        self._conn.send(b"(param-ref 'wavemeter:channel1:frequency)\n")
        _sleep(self.sleep_time)
        return float(self._conn.recv(1024).decode('utf-8')[:-2])
    def clear_buffer(self):
        try:
            self._conn.recv(1024)
        except _socket.timeout:
            pass

    def close(self):
        self._conn.close()
        _unregister(self.close)
        
    def __del__(self):
        try:
            self.close()
        except Exception as e:
            print(e)
        # _unregister(self.close)
