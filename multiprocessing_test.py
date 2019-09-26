from shg import SHGpro
from multiprocessing import Process
from multiprocessing.managers import BaseManager, NamespaceProxy

class MyManager(BaseManager):
    pass

class MyProxy(NamespaceProxy):
    _exposed_ = ('__getattribute__','__setattr__','__delattr__','dlc')

    def dlc(self):
        callmethod = object.__getattribute__(self,'_callmethod')
        return callmethod('dlc')

MyManager.register('SHGpro', SHGpro, MyProxy)

def get_shg_dl_piezo(shg:SHGpro):
    print(shg.get_dl_piezo())

if __name__ == "__main__":
    manager = MyManager()
    manager.start()
    shared = manager.SHGpro('192.168.1.2','COM4')

    input()
    p1 = Process(target=get_shg_dl_piezo,args=(shared,))
    p1.start()
    p1.join()
    p1.close()
    input('closed process')