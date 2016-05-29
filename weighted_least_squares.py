"""
Weighted least squares fitting to a straight line

"""

import numpy as np
import math
from pylab import *
import matplotlib.pyplot as plt

class Regress:


    def wregress(x,y,sy):
        sum_x_y,sum_x_sy2,sum_x2_sy2,\
                sy_inv,sum_y_sy2 = [],[],[],[],[]
        n = 0
        for i in x:
            sum_x_sy2.append(i* (float(sy[n])**-2))
            sum_x2_sy2.append((i**2)/float(sy[n])**2)
            sum_x_y.append((i * float(y[n])/
                                float(sy[n])**2))
            sum_y_sy2.append(float(y[n])/
                            float(sy[n])**2)
            sy_inv.append(float(sy[n])**-2)
            n += 1 
        
        A = column_stack((
                    [sum(sum_x2_sy2),sum(sum_x_sy2)],
                    [sum(sum_x_sy2),sum(sy_inv)]))
        b = [sum(sum_x_y),sum(sum_y_sy2)]
        a,b = dot(inv(A),b)

        return [a,b]

    x = arange(0,5,0.5)
    y = array([2.75,4.83,5.05,6.80,8.83,
                8.64,11.03,13.20,13.08,15.68]
                )
    sy = array([0.5,0.6,0.7,0.8,0.9,0.9,
                        1.0,1.1,1.1,1.2]
                )

    c = wregress(x,y,sy)

class Main:
    

    if __name__ == "__main__":

        x = arange(0,5,0.5)
        y = array([2.75,4.83,5.05,6.80,8.83,
                    8.64,11.03,13.20,13.08,15.68]
                    )
        sy = array([0.5,0.6,0.7,0.8,0.9,0.9,
                            1.0,1.1,1.1,1.2]
                    )
        print(Regress.c)
        plot(x,polyval(Regress.c,x),x,y,'o')
        show()


