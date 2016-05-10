"""

Estimating means from experimental data

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
    
    ym = cumsum(y)/(arrange(y.size) + 1) # Q2
    
    return None

part_one()
