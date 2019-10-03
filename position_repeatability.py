"""diagnostic script for coarse wavelength motor"""


from dlpromotor import *
import socket
from tqdm import tqdm
from time import sleep

class Wavemeter:
    def __init__(self,host,port=1998,timeout=1.0):
        self._host = host
        self._port = port
        self._conn = socket.create_connection((self._host,self._port),timeout=timeout)
    def measure_wavelength(self):
        self._conn.send(b"(param-ref 'wavemeter:channel1:wavelength)\n")
        sleep(0.1)
        return float(self._conn.recv(1024).decode('utf-8')[:-2])
    def measure_frequency(self):
        self._conn.send(b"(param-ref 'wavemeter:channel1:frequency)\n")
        sleep(0.1)
        return float(self._conn.recv(1024).decode('utf-8')[:-2])

def sweep_position_vs_wavelength(outfile,position_high,position_low,step_size=10):
    with open(outfile,'w') as f:
        wavemeter = Wavemeter('192.168.1.1')
        wavemeter._conn.recv(1024)
        f.write('position,wavelength (m),frequency (Hz), wavelength(nm), frequency (THz)\n')
        for pos in tqdm(range(position_low,position_high+step_size,step_size)):
            # print(get_position())
            set_position(pos)
            sleep(6.0)
            wavelength = wavemeter.measure_wavelength()
            freq = wavemeter.measure_frequency()
            f.write('{},{},{},{},{}\n'.format(pos,wavelength,freq,wavelength*1e9,freq/1e12))
        

def home():
    set_position(0)
    sleep(5.0)
    set_position(102000)
    sleep(5.0)

    
if __name__ == '__main__':
    import sys
    num_sweeps = int(sys.argv[1])
    home()
    # print('up')
    # sweep_position_vs_wavelength('sweep_{}_up.csv'.format(31),120000,110000,250)
    # print('down')
    # sweep_position_vs_wavelength('sweep_{}_down.csv'.format(32),110000,120000,-250)
    # print('up')
    # sweep_position_vs_wavelength('sweep_{}_up.csv'.format(33),120000,110000,250)
    try:
        for sweep_num in tqdm(range(num_sweeps)):
            if (sweep_num % 2) == 0:
                sweep_position_vs_wavelength('sweep_{}_up.csv'.format(sweep_num),122000,102000,250)
            else:
                sweep_position_vs_wavelength('sweep_{}_down.csv'.format(sweep_num),102000,122000,-250)
    except KeyboardInterrupt:
        pass
    set_position(110500)