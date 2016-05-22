"""
Finding the best straight line through a set of points

"""

import numpy as np
import math
from pylab import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


filename = 'test_data.txt'

def import_test_data(filename):
    file_object = (open(filename, 'r')).readlines()
    xdata = []
    ydata = [] 
    for line in file_object:
        line = line.split(";")
        xdata.append(float(line[0]))
        ydata.append(float(line[1]))
    return xdata,ydata
 
x,y = import_test_data(filename) 

#x = array([1,2,3,4,5,6,7])
#y = array([2,4,6,9,10,11,15]) 

def func(x, a, b):
    return a*x + b

def lregress(x, y):
    a,b = curve_fit(func, x, y)[0] 
    return [b,a]

print(lregress(x,y))

"""
from straight_line_plots import lregress
from straight_line_plots import import_test_data

"""
