#!/usr/bin/env python3
import numpy as np
import h5py

hf_exp=h5py.File('DataExperiment.h5','r')
enout_exp=hf_exp['enout_exp'][()]
s_exp=hf_exp['s_exp'][()]
enout_interp=hf_exp['enout_interp'][()]
hf_exp.close()

hf_result=h5py.File('DataResult.h5','r')
conversionResult=hf_result['conversionResult'][()]
hf_result.close()

Inte_conversionResult=np.trapz(conversionResult,enout_interp)
Nor_conversionResult=conversionResult/Inte_conversionResult
Inte_sExp=np.trapz(s_exp[::-1],enout_exp[::-1])
Nor_sExp=s_exp/Inte_sExp
#print(s_exp[::-1])
#print(enout_exp[::-1])
#print(Inte_conversionResult)
#print(Inte_sExp)

hf=h5py.File('NormalizationData.h5','w')
hf.create_dataset('Inte_conversionResult',data=np.array([Inte_conversionResult]))
hf.create_dataset('Nor_conversionResult',data=Nor_conversionResult)
hf.create_dataset('Inte_sExp',data=np.array([Inte_sExp]))
hf.create_dataset('Nor_sExp',data=Nor_sExp)
hf.create_dataset('enout_exp',data=enout_exp)
hf.create_dataset('enout_interp',data=enout_interp)
hf.close()
