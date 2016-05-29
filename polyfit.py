"""
Last Exercise on Polyfit

"""
import numpy
import math
from pylab import *
import matplotlib.pyplot as plt

x = arange(0,5,0.5)
y = array([2.75,4.83,5.05,6.80,\
            8.83,8.64,11.03,\
            13.20,13.08,15.68]
            )
sy = array([0.5,0.6,0.7,0.8,0.9,
            0.9,1.0,1.1,1.1,1.2]
            )
c,cov = polyfit(x,y,1,w=1/sy,cov=True)
plot(x,polyval(c,x),x,y,'o')

sc = sqrt(cov.diagonal())
print(c,sc)
errorbar(x,y,yerr=sy,fmt='o')

show()
