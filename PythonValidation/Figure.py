#!/usr/bin/env python3
import numpy as np
from scipy.interpolate import RectBivariateSpline
import h5py
import matplotlib.pyplot as plt

hf_exp=h5py.File('DataExperiment.h5','r')
enout_exp=hf_exp['enout_exp'][()]
s_exp=hf_exp['s_exp'][()]
enout_interp=hf_exp['enout_interp'][()]
theta_exp=hf_exp['theta_exp'][()]
hf_exp.close()

hf_result=h5py.File('DataResult.h5','r')
conversion_result=hf_result['conversionResult'][()]
hf_result.close()

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set(xlim=[0,np.max(enout_interp)],xlabel='Energy[eV]',ylabel='d2σ/dΩdE[beV-1sr-1]')
ax.semilogy(enout_interp,conversion_result,color='black',label='Calculation')
ax.scatter(enout_exp,s_exp,color='red',marker='+',label='nds theta=%.1f'%theta_exp[0])
ax.legend()
plt.show()
