# import zaber.serial
from zaber.serial import BinarySerial, BinaryCommand, BinaryReply, BinaryDevice
from math import floor
import numpy as np

PORTNAME = 'COM10'
BAUDRATE = 9600


GridSz = 9; # n x n grid
GridSz = GridSz + (1-(GridSz%2))
# At this point <numSpeckleMeasurements> is ODD
arr1D = np.arange(-floor(GridSz - 1)//2,1+floor(GridSz - 1)//2)
numSpeckleMeasurements = GridSz**2

ZaberGimbalAngularResolution = 0.02
# Horizontal
ZaberGimbalWStartPosition = -42.31
# Vertical
ZaberGimbalUStartPosition = -5.14

Horizontal_Angle_Unique = ZaberGimbalWStartPosition + arr1D * ZaberGimbalAngularResolution
Horizontal_Starting_Angle = Horizontal_Angle_Unique[0]
Horizontal_Ending_Angle = Horizontal_Angle_Unique[-1]

Vertical_Angle_Unique = ZaberGimbalUStartPosition + arr1D * ZaberGimbalAngularResolution
Vertical_Starting_Angle = Vertical_Angle_Unique[0]
Vertical_Ending_Angle = Vertical_Angle_Unique[-1]

Horizontal_Steps = np.zeros(numSpeckleMeasurements,1)
Vertical_Steps = np.zeros(numSpeckleMeasurements,1)

zaber = BinarySerial(PORTNAME)

