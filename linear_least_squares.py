"""
Linear least-squares model fitting

"""

import numpy
import math
from pylab import *
import matplotlib.pyplot as plt

def data(filename):
    file_object = (open(filename, 'r')).readlines()
    xdata = []
    ydata = [] 
    for line in file_object:
        line = line.split(";")
        xdata.append(float(line[0]))
        ydata.append(float(line[1]))
    return xdata,ydata

def mregress(x,y):
    n = 0
    col_2 = []
    while n < len(x):
        col_2.append(1)
        n +=1
    A = column_stack((array(x),array(col_2)))
    a,b = solve(dot(transpose(A),A),dot(transpose(A),y))
    return [b,a]

def main():
    filename = 'test_data.txt'
    x,y = data(filename)
    print(mregress(x,y))

main()

"""
from linear_least_squares import mregress 

"""
