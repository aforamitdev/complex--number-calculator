# --------------
#Code starts here
import pandas as pd
import numpy as np
import math
class complex_numbers:
    

    def __init__(self,real,imag):
        
        self.real=real
        self.imag=imag
        
    
    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    
    def __add__(self,other):
        a=self.real+other.real
        v=self.imag+other.imag
        return complex_numbers(a,v)

    def __mul__(self,other):
        return complex_numbers(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
        
    def __sub__(self,other):
        a=self.real-other.real
        v=self.imag-other.imag
        return complex_numbers(a,v)
    
    def __truediv__(self,other):
        pass        
    def absolute(self):

        return abs(self) 
    def argument(self):
        return np.angle(self, deg=True) 

    def conjugate(self):
        return self.conjugate()


        
        
comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1+comp_2



comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=1+0.25j

comp_arg=round(complex_numbers.argument(3+5j),2)
comp_abs=complex_numbers.absolute(3+5j)
comp_conj=complex_numbers.conjugate(3+5j)




