import numpy as np 
from .utils import alpha_PM, beta_PM, gamma_JONSWAP
from scipy.constants import g


def PiersonMoskowitz(omega, U_195:float=10, alpha:float=alpha_PM, beta:float=beta_PM, g:float=g) : 
    return ((alpha * (g ** 2)) / (omega ** 5)) * np.exp(-beta * ((g / (U_195*omega)) ** 4))

def JONSWAP(omega, U_10:float=10, F:float=30e3, gamma:float=gamma_JONSWAP, g:float=g) : 
    
    X = g*F/(U_10**2)
    alpha = 0.076 * X**(-0.22)
    omega_p = 22*(g/U_10)*X**(-1/3)
    
    sigma = 0.07 if omega <= omega_p else 0.09
    r = np.exp(-(((omega-omega_p)**2)/(2*(sigma*omega_p)**2)))
    
    return ((alpha*(g**2))/(omega**5))*np.exp((-5/4)*(omega_p/omega)**4)*(gamma**r)