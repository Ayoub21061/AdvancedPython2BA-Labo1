import numpy as np
import math
from scipy import integrate

def fact(n): # Fonction factorielle 
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def roots(m):
    polynomial_roots = np.roots(m)
    return polynomial_roots

coefficients = [1, -3, 2]  # Polynôme x^2 - 3x + 2
polynomial_roots = roots(coefficients)

def f(x):
    return (math.sin(x))

def integral():
    result, error = integrate.quad(f, 1, 1)
    return result 



     