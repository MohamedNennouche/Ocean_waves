# constants
## Pierson Moskowitz
alpha_PM = 8.1e-3
beta_PM = 0.74
## JONSWAP
gamma_JONSWAP = 3.3


# conversion utils
def U_10_to_U_195(U_10) : 
    return U_10 * 1.026

def U_195_to_U_10(U_195) : 
    return U_195/1.026

def wind_speed_weibull() : 
    return 0