#!/usr/bin/env python3
import numpy as np
import h5py
import sys
sys.path.append(r'/home/ni/git/ReadTxtData/PythonReadTxtData')
from ReadTXT import ReadTxt

read15=ReadTxt('/home/ni/ReadData/X4sGetSubentLightWater2.txt',55.0,15.0) # energy-in(meV) angle
read15.readData()

