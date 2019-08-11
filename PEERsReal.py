################################################### PEERs equation solver in 1 variable 
#                                                   and in the set of real numbers

# author: Roberto Bastone
# email: robertobastone93@gmail.com

version = 1.00

################################################### Packages

import numpy as np
import matplotlib.pyplot as plt
from termcolor import colored
import string
alphabet = list(string.ascii_lowercase)  # the whole latin alphabet

################################################### CODE

class PEERsReal:
    yes = {'Y','y'}
    no = {'N','n'}
    def __init__(self):
        print colored("Initializing...PEERsReal version " + str(version), 'blue')
        print colored("Welcome to the Pythonic Easy Equation Resolver (PEER) in 1 variable version " + str(version), "blue")
        
    def main(self):
        canWeContinue = False
        while canWeContinue == False:
            degree, polynomial = self.writePolynomial()
            canWeContinue = self.checkPolynomial(self.yes,self.no)
        x, roots = self.plotPolynomial(polynomial)
        self.classifyRootsPolynomial(degree, x, roots)
        
    def writePolynomial(self):
        while True:
            coefficients = []
            try:
                PolyDegree = int(raw_input(">What is the degree of the polynomial? \n"))
                for i in range (0,PolyDegree+1):
                    while True:
                        try:
                            coefficients.append( float(input(">Type the value of the coefficient " + alphabet[i] + " of the term x^" + str(PolyDegree - i) + " ")) )
                            break
                        except:
                            print colored("Error! You must choose a number", 'red')            
                polynomial = np.poly1d(coefficients)
                print ">The equation you have typed in is as follows:"
                print(polynomial)
                return PolyDegree, polynomial
            except:
                print colored("Error! You must choose a number", 'red')            
    
    def checkPolynomial(self,yes,no):        
        while True:
            choice = raw_input(">Is this your equation? [y/n] \n")
            if choice in yes:
               print">Okay, let us continue"
               #break
               return True
            elif choice in no:
                #self.writePolynomial()
                return False
            else:
                print( colored(">Please, select [y/n] only",'yellow'))
                continue

    def plotPolynomial(self,polynomial):       
        print">Let us plot the polynomial. Choose the range in the x."
        while True:
            try:
                x_min = float(raw_input(">Choose x min: "))
                x_max = float(raw_input(">Choose x max: "))
                break
            except:
                print colored("Error! You must choose a number", 'red')            
        x = np.linspace(x_min,x_max, 1e5 )
        roots_indexes = np.argwhere(np.diff(np.sign(0 - polynomial(x)))).flatten()
        
        plt.figure(figsize=(10,10))
        plt.axvline(0, color='black', zorder = 3)
        plt.axhline(0, color='black', zorder = 2)
        plt.ylabel('y')
        plt.xlabel('x')
        plt.xlim(x_min,x_max)
        plt.ylim(x_min,x_max)
        plt.plot(x,polynomial(x) , zorder = 1)
        plt.scatter(x[roots_indexes],polynomial(x[roots_indexes]),marker='x', color='red', zorder = 4)
        plt.show()
        return x, roots_indexes 
        
    def classifyRootsPolynomial(self, PolyDegree, x, roots_indexes):
        for i in range (0,len(roots_indexes)):
            print ">We have a root for x=", round(x[roots_indexes[i]],5)
        if (PolyDegree - len(roots_indexes) == 0) :
            print colored(">We have found all "+ str(len(roots_indexes))  + " roots", 'green')
        else:
            print ">This means that we have", PolyDegree - len(roots_indexes), "roots that are either complex or not inside the range investigated."