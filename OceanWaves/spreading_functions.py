import numpy as np

def ittc(thetas:np.array) : 
    return (2/np.pi)*np.cos(thetas)**2

def issc(thetas:np.array) :
    return (8/(3*np.pi))*np.cos(thetas)**4

def swop(thetas:np.array, omega:float, U:float, g:float=9.81) :
    p = 0.5 + 0.82*np.exp(-0.5*((omega*U)/g)**4)
    q = 0.32*np.exp(-0.5*((omega*U)/g)**4)
    
    D = (1/np.pi)*(1 + p*np.cos(2*thetas) + q*np.cos(4*thetas))
    
    return D

def eckv_spreading_function() : 
    return 0