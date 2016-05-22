"""
Linear least-squares model fitting

"""

import numpy
import math
from pylab import *
import matplotlib.pyplot as plt
from straight_line_plots import import_test_data

def mregress(x,y):
    A = column_stack((array(x),array(y)))
    result = solve(dot(transpose(A),A),dot(transpose(A),y))
    return result

def main():
    filename = 'test_data.txt'
    x,y = import_test_data(filename)

    print(mregress(x,y))

main()

"""
from linear_least_squares import mregress 

"""
