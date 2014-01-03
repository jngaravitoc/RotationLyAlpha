import math
import numpy as np

def escape_slab(tau_0, tau_d, albedo, a):
    escape = (a * tau_0)**(1.0/3.0)
    escape = escape * (1.0 - albedo) * tau_d
    escape = escape**(0.5)
    xi_prime = math.sqrt(3.0)/(math.pi**(5.0/12.0))
    xi_prime = xi_prime/0.525    
    escape = 1.0/math.cosh(xi_prime * escape)
    return escape

def escape_cube(tau_0, tau_d, albedo, a):
    eta = 0.71
    escape = (a * tau_0)**(1.0/3.0)
    escape = escape * (1.0 - albedo) * tau_d
    escape = (eta**(4.0/3.0) * escape)**(0.55)
    xi_prime = math.sqrt(3.0)/(math.pi**(5.0/12.0))
    xi_prime = xi_prime/0.525    
    escape = 1.0/math.cosh(xi_prime * escape)
    return escape
    

tau_0=np.array([1E5, 1E6, 1E7])

for item in tau_0:
    l = escape_slab(item, 1.0, 0.5, 4.7E-4)
    c = escape_cube(item, 1.0, 0.5, 4.7E-4)
    print l,c
