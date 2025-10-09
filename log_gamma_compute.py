#coding:utf-8

#  compute  Log(gamma(1/2+i*T)) 
#
#  log r*e(i*Q) = log r + i*Q

import mpmath
import numpy as np
import matplotlib.pyplot as plt


T1=66
T2=0
delta0=0.1

step0=int((T1 - T2)/delta0)
yl=np.arange(step0+1, dtype='float64') * delta0 + T2

mpmath.mp.dps = 20

#(1) Log gamma(s) directly
gamma_real=np.zeros(len(yl))
gamma_imag =np.zeros(len(yl))
gamma_net_imag =np.zeros(len(yl))

#(2) log(F)= (s - 0.5) * mpmath.log(s) - s + O(1) usin Laplace-Stirling asymptotic
zenkin_real=np.zeros(len(yl))
zenkin_imag =np.zeros(len(yl))

kaiten=0
for i in range(len(yl)):
    t=0.5 + yl[i]*1J
    #(1)
    a=mpmath.log( mpmath.gamma(t))
    gamma_real[i]=np.float64(a.real)
    gamma_imag[i]=np.float64(a.imag)
    
    # net change
    if i > 0 and gamma_imag[i-1] > 0 and gamma_imag[i] < 0:
        kaiten +=1
    gamma_net_imag[i]= gamma_imag[i] + 2 * np.pi * kaiten
    
    #(2)
    a= (t - 0.5) * mpmath.log(t) - t
    #a=(t/2.0) * mpmath.log( t / mpmath.pi /2.) - t/2 - mpmath.pi/8 + 1/48./t
    zenkin_real[i]=np.float64(a.real)
    zenkin_imag[i]=np.float64(a.imag)



# plot value
fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111)
ax.set_title(" value of log gamma(1/2+i*T)", size = 14)
ax.grid()
#ax.set_xlim(0, 40)
#ax.set_ylim(-5, 5)
ax.set_xlabel("T")
ax.set_ylabel("value")
ax.plot(yl, gamma_real, color = "yellow", label="mpmath.log real",linestyle="dashed")
ax.plot(yl, gamma_imag, color = "black",  label="mpmath.log imag")
ax.plot(yl, gamma_net_imag, color = "cyan",  label="mpmath.log imag, net change")
ax.plot(yl, zenkin_real, color = "green", label="(s-0.5)log(s)-s+O(1), real",linestyle="dotted")
ax.plot(yl, zenkin_imag, color = "red",  label="(s-0.5)log(s)-s+O(1), imag",linestyle="dotted")
ax.legend()
plt.show()
