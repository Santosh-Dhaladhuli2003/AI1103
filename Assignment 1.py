# -*- coding: utf-8 -*-
"""Assigment-1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dP9yekjZMsQ_OR84k0LQa-5Q2S3bjOTR
"""

import math
import numpy as np
import scipy as sp
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sn
import xlrd






print("Given, P(X=0) = 0")
print("Given, P(X=1) = k")
print("Given, P(X=2) = 2k")
print("Given, P(X=3) = 2k")
print("Given, P(X=4) = 3k") 
print("Given, P(X=5) = k^2")
print("Given, P(X=6) = 2k^2")
print("Given, P(X=7) = 7k^2 + k")


print ("\n Sum of probabilities in a Probability Distribution is always equal to 1 \n")

print (" \n So,  0 + k + 2k + 3k + k^2 + 2k^2 + (7k^2 + k) = 1 \n")

print("\n Implies, 10k^2 + 9k - 1 = 0 \n")

print("\n This is quadratic equations , let a,b and c be its coefficients.\n")

a = 10
b = 9
c = -1

D = math.sqrt(b**2 - 4*a*c)

print ("Let p and q be the roots. ")

p = (-b + D)/(2*a)
q = (-b - D)/(2*a)





print("Since k = {0} is negative, its not possible".format(q))
print ("Therefore k = {0}".format(p))
 
r = 7*p*p + p
f = 0
g = 2*p
h = f + p + g
i = p + g
j = p*p
v = 2*j
t = h + g
u = t + i
z = u + j
w = v + z

print("P(X < 3) = P(X=2) + P(X=1) + P(X=0) = {0}".format(h))
 

print("P(X > 6) = P(X = 7) = {0}".format(r))

print("P(0 < X < 3) = P(X=2) + P(X=1) = {0}".format(i))

#plotting the probability

pmf = [f,p,g,g,i,j,v,r]


X = [0,1,2,3,4,5,6,7]

 

# set the x axis and y axis limits

pylab.xlim([0,8])

pylab.ylim([0,1])

 

# Provide a title for the stem plot

plt.title('PMF')

 

# Give x axis label for the stem plot

plt.xlabel('X')

 

# Give y axis label for the stem plot

plt.ylabel('Pr(X)')

 

# plot the stem plot using matplotlib

markerline, stemlines, baseline = plt.stem(X, pmf, '-')

 

# display the stem plot

plt.show()



cdf = [f,p,h,t,u,z,w,1]


X = [0,1,2,3,4,5,6,7]

 

# set the x axis and y axis limits

pylab.xlim([0,8])

pylab.ylim([0,1.2])

 

# Provide a title for the stem plot

plt.title('CDF')

 

# Give x axis label for the stem plot

plt.xlabel('X')

 

# Give y axis label for the stem plot

plt.ylabel('F(X)')

 

# plot the stem plot using matplotlib

markerline, stemlines, baseline = plt.stem(X, cdf, '-')

 

# display the stem plot

plt.show()


















 







