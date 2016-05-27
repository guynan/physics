"""
Finding the best straight line through a set of points

"""

import numpy as np
import math
from pylab import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class ImportTest:
   
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


class Regress(ImportTest):

    x = ImportTest.x
    y = ImportTest.y

    def lregress(x,y):
        run_sum = []
        n = 0
        for i in x:
            run_sum.append(i * float(y[n]))
            n += 1 
        sum_x_y = sum(run_sum)        
        
        tot = []
        for v in x:
            tot.append(v**2)
        A = column_stack((
                    [sum(tot),sum(x)],
                    [sum(x),len(x)]))
        b = [sum_x_y,sum(y)]
        a,b = dot(inv(A),b)

        return [b,a]
       
    result = lregress(x,y) 

class Main:

    if __name__ == "__main__":
        
        x = array([ImportTest.x])
        y = array([ImportTest.y])
        xd = ImportTest.x
        yd = ImportTest.y
        b,a = Regress.result 
        eq = a*x +b
        plot(x,eq,'co')
        plot(xd,yd)
        print(b,a) 
        show() 
Main()
