#!/usr/bin/env python3
import numpy as np
import h5py
import matplotlib.pyplot as plt

hf_exp=h5py.File('DataExperiment.h5','r')
theta_exp=hf_exp['theta_exp'][()]
hf_exp.close()

hf_nor=h5py.File('NormalizationData.h5','r')
enout_exp=hf_nor['enout_exp'][()]
Nor_sExp=hf_nor['Nor_sExp'][()]
Inte_sExp=hf_nor['Inte_sExp'][()]
enout_interp=hf_nor['enout_interp'][()]
Nor_conversionResult=hf_nor['Nor_conversionResult'][()]
Inte_conversionResult=hf_nor['Inte_conversionResult'][()]
hf_nor.close()

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax1.set(xlim=[0,np.max(enout_interp)],xlabel='Energy(eV)')
ax1.semilogy(enout_interp,Nor_conversionResult,color='black',label='Calculation,%f'%Inte_conversionResult[0])
ax1.scatter(enout_exp,Nor_sExp,color='red',marker='+',label='nds theta=%.1f,%f'%(theta_exp[0],Inte_sExp[0]))
ax1.legend()
ax2=fig.add_subplot(1,2,2)
ax2.set(xlim=[0,np.max(enout_interp)],xlabel='Energy(eV)')
ax2.plot(enout_interp,Nor_conversionResult,color='black',label='Calculation,%f'%Inte_conversionResult[0])
ax2.scatter(enout_exp,Nor_sExp,color='red',marker='+',label='nds theta=%.1f,%f'%(theta_exp[0],Inte_sExp[0]))
ax2.legend()
plt.show()
