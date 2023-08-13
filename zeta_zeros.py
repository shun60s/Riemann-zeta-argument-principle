#coding:utf-8

# According to argument principle, the number of zeros and poles inside of 
# rectangle area of Riemann zeta function is calculated, integral by piecewise quadrature method.
# Due to calculation error occurs, result which means the difference between the number 
# of zeros and poles, becomes complex number, almost integer. 
#
# example 1
#  first 5 non-trivial zero points of Riemann zeta function
#   14.134j + 1/2
#   21.022j + 1/2
#   25.010j + 1/2
#   30.424j + 1/2
#   32.935j + 1/2
# example 2
#  includes 1+j0  pole.


import math
import mpmath
import numpy as np

# Python 3.6.4 on windows 10
# mpmath 1.1.0
# numpy  1.19.5


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Riemann zeta function and argument principle')
    parser.add_argument('--delta','-d', type=float, default=0.01, help='piecewise quadrature step')
    parser.add_argument('--x0','-x', type=float, default=0.0, help='horizontal position')
    parser.add_argument('--x1','-y', type=float, default=1.0, help='horizontal position')
    parser.add_argument('--y0','-a', type=float, default=0.1, help='vertical position')
    parser.add_argument('--y1','-b', type=float, default=33.0, help='vertical position')
    args = parser.parse_args()
    
    # define rectangle
    #w0=[0.0, 1.0]  # rectangle horizontal is critical strip, real number
    #h0=[1.0, 33.0] # rectangle vertical is first 5 non-trivial zeros area, imaginary number
                    #                       starts 1.0 to avoid pole 1+j0
    w0=[ args.x0, args.x1 ]
    h0=[ args.y0, args.y1 ]
    print("vertical horizontal",h0,w0)
    
    # define piecewise quadrature step of integral
    #delta0=0.01
    delta0= args.delta
    print("piecewise quadrature step", delta0)
    
    #
    hd=int((h0[1]-h0[0])/delta0)
    wd=int((w0[1]-w0[0])/delta0)
    print("vertical horizontal division number", hd, wd)
    
    # get dividing points along rectangle
    yp=np.arange(hd+1, dtype='float64') * delta0
    xp=np.arange(wd+1, dtype='float64') * delta0
    
    c1=(w0[1]+ 1j * h0[0]) +  1j * yp
    c2= c1[-1] - xp
    c3= c2[-1] - 1j * yp
    c4= c3[-1] + xp
    
    c_all_plus_last=np.concatenate([c1[:-1],c2[:-1],c3[:-1],c4])
    
    b1= np.ones(hd) * delta0 * 1j
    b2= np.ones(wd) * delta0
    
    b_all_half=np.concatenate([b1,b2 * -1 ,b1 * -1 ,b2]) / 2.0  # 1/2.0 means to get average
    
    # show dividing points if 1
    if 0:
        for i in range(len(c_all_plus_last)-1):
            print(i,c_all_plus_last[i],b_all_half[i] * 2.0)
        print(c_all_plus_last[-1])
    
    # integral by piecewise quadrature method
    rtn=mpmath.mpf(0.0)
    stack0=mpmath.fdiv(mpmath.zeta(c_all_plus_last[0], derivative=1),mpmath.zeta(c_all_plus_last[0]))
    for i in range(len(c_all_plus_last)-1):
        stack1=mpmath.fdiv(mpmath.zeta(c_all_plus_last[i+1], derivative=1),mpmath.zeta(c_all_plus_last[i+1]))
        rtn=mpmath.fadd(mpmath.fmul(mpmath.fadd(stack0,stack1), mpmath.mpmathify(b_all_half[i])),rtn)
        stack0=mpmath.mpmathify(stack1)
        
    sekibun= rtn / (2.0 * math.pi * 1j)
    
    # show result which means the difference between the number of zeros and poles inside rectangle area
    print('result', sekibun)
