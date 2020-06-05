# Author : koshvendra Singh
# Date   : 05/06/2020
# Email  : koshvendra.singh@tifr.res.in
# Description : solving IVP simultaneous differential equation
# y1'=32y1 + 66y2 + 2x/3 + 2/3  && y2'=-66y1 -133y2 -x/3 1/3   && 0<=x<=0.5,y1(0)=1/3,y2(0)=1/3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# solving system of differential equation by 'RK45' method
def f(x,r):
    y1,y2=r
    fy1= 32*y1 + 66*y2 + (2/3)*x + 2/3
    fy2= -66*y1 - 133*y2 - x/3 - 1/3
    return fy1,fy2

x_range=(0,0.5)
initial_val=(1/3,1/3)

sol = solve_ivp(f,x_range,initial_val)
y1,y2 = sol.y
x = sol.t

# solving system of differential equation by 'BDF'(backward differentiation formula) method
def g(x,r):
    y1,y2=r
    fy1= 32*y1 + 66*y2 + (2/3)*x + 2/3
    fy2= -66*y1 - 133*y2 - x/3 - 1/3
    return fy1,fy2

x_range=(0,0.5)
initial_val=(1/3,1/3)

sol = solve_ivp(g,x_range,initial_val,method='BDF')
y3,y4 = sol.y
x2 = sol.t

# plotting
fig,(ax1,ax2)=plt.subplots(1,2)
plt.suptitle('solution of prob6')
ax1.plot(x,y1,'b',label='y1')
ax1.plot(x,y2,'black',label='y2')
ax1.set(xlabel='x',ylabel='y1,y2')
ax1.set_title('solving by RK45')

ax2.plot(x2,y3,'b',label='y1')
ax2.plot(x2,y4,'black',label='y2')
ax2.set_title('solving by BDS method')
ax2.set(xlabel='x',ylabel='y1,y2')

plt.subplots_adjust(wspace=0.6)

plt.legend()
plt.show()
