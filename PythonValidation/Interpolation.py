import numpy as np
from scipy.interpolate import RectBivariateSpline
import h5py
import matplotlib.pyplot as plt

const_planck = 4.13566769692386e-15  # (source: NIST/CODATA 2018)
const_hbar = const_planck*0.5/np.pi  # [eV*s]

hf_sqwCal=h5py.File('/home/ni/ReadData/corr.sqw','r')
sCal=np.array(hf_sqwCal['sqw']) # 2-D array with shape (250,2097152)
point_qCal=np.array(hf_sqwCal['qVec'])  # 1-D array with shape (250,)
point_wCal=np.array(hf_sqwCal['omega']) # 1-D array with shape (2097152,)
hf_sqwCal.close()

hf_sqwInterp=h5py.File('DataInterpolatedPoints.h5','r')
qInterp=hf_sqwInterp['q_interp'][()]
wInterp=hf_sqwInterp['omega_interp'][()]
conversion_parameter=hf_sqwInterp['conversion_parameter'][()]
hf_sqwInterp.close()


sInterpolate=RectBivariateSpline(point_qCal,point_wCal,sCal)
resultInterpolate=sInterpolate.ev(qInterp,wInterp)
conversion_result=resultInterpolate*conversion_parameter
print(conversion_result.shape)

hf_result=h5py.File('DataResult.h5','w')
hf_result.create_dataset('conversionResult',data=conversion_result)
hf_result.close()
