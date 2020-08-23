import numpy as np


#default units:
#energy eV
#wavelength angstrom
#time second
#wavenumber angstrom^-1
#angle degree

const_angstrom = 1.
const_second = 1.
const_ps = const_second*1e-12
const_fs = const_second*1e-15
const_planck = 4.13566769692386e-15  #(source: NIST/CODATA 2018)
const_hbar = const_planck*0.5/np.pi  #[eV*s]
const_radpsec2eV = const_hbar
const_eV2radpsec = 1./const_radpsec2eV
const_radpsec2meV = const_radpsec2eV*1e3
const_radpfs2meV = const_radpsec2meV*1e15

const_deg2rad = np.pi/180.
const_eV2kk = 1/2.072124652399821e-3
const_c  = 299792458e10 # speed of light in Aa/s
const_dalton2kg =  1.660539040e-27  # amu to kg (source: NIST/CODATA 2018)
const_dalton2eVc2 =  931494095.17  # amu to eV/c^2 (source: NIST/CODATA 2018)
const_avogadro = 6.022140857e23  # mol^-1 (source: NIST/CODATA 2018)
const_boltzmann = 8.6173303e-5   # eV/K
const_neutron_mass = 1.674927471e-24  #gram
const_neutron_mass_evc2 = 1.0454075098625835e-28  #eV/(Aa/s)^2  #fixme: why not calculated from other constants).#<EXCLUDE-IN-NC1BRANCH>
const_neutron_atomic_mass = 1.00866491588  #atomic unit
const_ekin2v = np.sqrt(2.0/const_neutron_mass_evc2)  #multiply with sqrt(ekin) to get velocity in Aa/s#<EXCLUDE-IN-NC1BRANCH>

def angularFre2eKin(fre):
    return fre*const_radpsec2eV

def eKin2AngularFre(en):
    return en*const_eV2radpsec

def eKin2k(eV):
    return np.sqrt(eV*const_eV2kk)

def k2eKin(wn):
    return wn*wn/const_eV2kk

def q2Alpha(Q, kt):
    return Q*Q/(kt*const_eV2kk)

def alpha2Q(alpha,kt):
    return np.sqrt(alpha*kt*const_eV2kk)

def angle2Q(angle, enin_eV, enout_eV):
    ratio = enout_eV/enin_eV
    k0=eKin2k(enin_eV)
    scale = np.sqrt(1.+ ratio - 2*np.cos(angle*const_deg2rad) *np.sqrt(ratio) )
    return k0*scale

def angle2Alpha(angle, enin_eV, enout_eV, kt):
   return (enin_eV + enout_eV - 2*np.sqrt(enin_eV * enout_eV)*np.cos(angle*const_deg2rad))/kt
