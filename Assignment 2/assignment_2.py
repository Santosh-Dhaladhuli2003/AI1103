# -*- coding: utf-8 -*-
"""Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jySVMore10N9eaQ6K9CuZ5Fl8__fYWMO
"""

import math
import random as rd
import numpy as np
import matplotlib.pyplot as plt


print("There are 52 complete weeks in a leap year")
a = 52
b = 7
c = a*b
d = 366 - c
e = d/b

print("So they will be 52 saturdays for sure")
print("Remaining days = 366 - 364 = 2 ")
print("So the probability of occurence of a  53rd Saturday is {0}".format(e))


