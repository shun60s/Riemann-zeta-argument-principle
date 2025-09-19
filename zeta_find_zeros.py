#coding:utf-8


#  Get  non-trivial zero points of Riemann zeta function by using mpmath built-in functions
#   14.134j + 1/2
#   21.022j + 1/2
#   25.010j + 1/2
#   30.424j + 1/2
#   32.935j + 1/2



import math
import mpmath
import numpy as np

# Python 3.6.4 on windows 10
# mpmath 1.1.0
# numpy  1.19.5

for i in range(100):
    z1a=mpmath.zetazero(i+1)
    # adjust tolerance of findroot start point without error
    tolerance1img= 1.0 / (i/2+1)  # this is an example.
    tolerance1real=0.3 / (i/50+1) # this is an example.
    z1b=mpmath.findroot(mpmath.zeta, z1a + tolerance1real - tolerance1img * 1j)
    
    
    # use Z-function (Riemann-Siegel Z function)
    if i == 0:
        g1 = 10.0 # this is an example.
        g2 = mpmath.grampoint(0)
    else:  # get Gram points 
        g1 = mpmath.grampoint(i-1)
        g2 = mpmath.grampoint(i)
    
    z1c=mpmath.findroot(mpmath.siegelz, [g1, g2], solver='bisect')
    
    
    print ('no.',i+1,  z1a, z1b, ' ',  z1c, g1 , g2)
    
    
    
    






