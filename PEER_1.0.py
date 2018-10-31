# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:10:21 2018

author: Roberto Bastone

email: robertobastone@gmail.com

"""

version = 1.0

# PACKAGES
import numpy as np
import matplotlib.pyplot as plt
import string
alphabet = list(string.ascii_lowercase)  # the whole latin alphabet

coefficients = []

print ">Welcome to the Pythonic Easy Equation Resolver (PEER) in 1 variable version ", version 
PolyDegree = int(raw_input(">What is the degree of the polynomial? \n"))

for i in range (0,PolyDegree+1):
     coefficients.append( float(input(">Type the value of the coefficient " + alphabet[i] + " of the term x^" + str(PolyDegree - i) + " ")) )

polynomial = np.poly1d(coefficients)
     
print ">The equation you have typed in is as follows:"
print(polynomial)


yes = {'Y','y'}
no = {'N','n'}

while True:
    choice = raw_input(">Is this your equation? [y/n] \n")
    if choice in yes:
       print">Okay, let us continue"
       break
    elif choice in no:
        print">Okay, start over the script"
        exit()
    else:
        print(">Please, select [y/n] only")
        continue

print">Let us plot the polynomial. Choose the range in the x."
x_min = int(raw_input(">Choose x min: "))
x_max = int(raw_input(">Choose x max: "))
        
x = np.linspace(x_min,x_max, 1e5 )
#zeroes = np.zeros((np.abs(x_min)+np.abs(x_max))*10)
roots_indexes = np.argwhere(np.diff(np.sign(0 - polynomial(x)))).flatten()

plt.figure(figsize=(10,10))
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x,polynomial(x))
plt.scatter(x[roots_indexes],polynomial(x[roots_indexes]),marker='x', color='red')
plt.show()

for i in range (0,len(roots_indexes)):
    print ">We have a root for x=", x[roots_indexes]

if (PolyDegree - len(roots_indexes) == 0) :
    print ">We have found all the roots."
else:
    print ">This means that we have", PolyDegree - len(roots_indexes), " roots that are either complex or not inside the range investigated."
