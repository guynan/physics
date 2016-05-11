"""

Estimating means from experimental data
This one is done

"""

import numpy
import math
from pylab import *
import matplotlib.pyplot as plt


def part_one():
    y = normal(25,3,20)
    z = normal(15,2,200)
    """ 
    print(y)
    count = 0
    for i in y:
        if 28 > i > 22:
            count +=1        
    print(count)
    """
    plot(z)
    show()

#part_one()

def part_two():
    
    for i in range(20):
        z = normal(15,3,200)
        zm = cumsum(z)/(arange(z.size) + 1)

        plot(zm)

    n = arange(1,200)
    su = 15+2/sqrt(n)
    sl = 15-2/sqrt(n)
    plot(su, 'b')
    plot(sl, 'b')
    su = 15+4/sqrt(n)
    sl = 15-4/sqrt(n)
    plot(su,'r')
    plot(sl,'r')
    
    show()
    
    return    

part_two()

