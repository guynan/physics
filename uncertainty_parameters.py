"""
Uncertainties in the parameters (p6)

"""

import numpy
import math
from pylab import *
import matplotlib.pyplot as plt
from weighted_least_squares import Regress as wls

"""
For brevity, I have defined mu as the sum of x**2/sigma**2
and have defined phi as the sum of inverse of sigma. 
The advantage here is that those values are calculated
ONCE and makes for *hopefully* more readable code.

In turn, this makes sigma**2(a) = delta ** -1 * mu
                    sigma**2(b) = delta ** -1 * phi
                    delta = phi * mu - (mu ** 2)
"""

def cerror(x,y,sy):
    mu,phi,delta = [],[],[]
    n = 0
    for i in x:
        mu.append((i**2)/ float(sy[n])**2)
        phi.append(float(sy[n])**-2)
        n +=1
    phi = float(sum(phi))
    mu = float(sum(mu))
    delta = abs((mu * phi) - (mu **2))
    sa = ((delta ** -1) * mu) ** 0.5
    sb = ((delta ** -1) * phi) ** 0.5
    
    return [sa,sb]


x = arange(0,5,0.5)
y = array([2.75,4.83,5.05,6.80,\
            8.83,8.64,11.03,\
            13.20,13.08,15.68]
            )
sy = array([0.5,0.6,0.7,0.8,0.9,
            0.9,1.0,1.1,1.1,1.2]
            )

c = wls.c 
plot(x,polyval(c,x),x,y,'o');
print(cerror(x,y,sy))
errorbar(x,y,yerr=sy,fmt='o')

show()

