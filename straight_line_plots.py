"""
Finding the best straight line through a set of points

"""

import numpy as np
import math
from pylab import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class ImportTest():
   
    def data(filename):
        file_object = (open(filename, 'r')).readlines()
        xdata = []
        ydata = [] 
        for line in file_object:
            line = line.split(";")
            xdata.append(float(line[0]))
            ydata.append(float(line[1]))
        return xdata,ydata
    
    filename = 'test_data.txt'
    x,y = data(filename)


def main():

    x = ImportTest.x
    y = ImportTest.y

    def func(x, a, b):
        return a*x + b

    def lregress(x, y):
        a,b = curve_fit(func, x, y)[0] 

        return [b,a]

    print(lregress(x, y)) 

main()

