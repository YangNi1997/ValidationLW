#!/usr/bin/env python3
import numpy as np
import h5py
from ConversionFunction import *
#default units:
#energy eV
#wavelength angstrom
#time second
#wavenumber angstrom^-1
#angle degree
#cross section barn
const_CrossSectionH1=82.03

hf_data=h5py.File('DataExperiment.h5','r')
enout_interp=hf_data['enout_interp'][()]
enin_exp=hf_data['enin_exp'][()][0]
theta_exp=hf_data['theta_exp'][()][0]
hf_data.close()

conversion_parameter=2*const_CrossSectionH1*np.sqrt(enout_interp/enin_exp)/const_hbar/(4*np.pi)
enout_interp2AngularFre=eKin2AngularFre(enout_interp)
enin_exp2AngularFre=eKin2AngularFre(enin_exp)
omega_interp=enin_exp2AngularFre-enout_interp2AngularFre
q_interp=angle2Q(theta_exp[()],enin_exp,enout_interp)

hf=h5py.File('DataInterpolatedPoints.h5','w')
hf.create_dataset('q_interp',data=q_interp)
hf.create_dataset('omega_interp',data=omega_interp)
hf.create_dataset('conversion_parameter',data=conversion_parameter)
hf.close()
