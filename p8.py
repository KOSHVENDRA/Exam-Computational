# Author : Koshvendra Singh
# date   : 05/06/2020
# Email  : koshvendra.singh@tifr.res.in
# Description : solving second order boundary value problem
# y''= 4(y-x)   , 0 <= x <= 1  , y(0)=0 , y(1)=2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# converting 2nd order diff equation to two first order diff equation 
def func(x,y):
    return np.vstack(( y[1] , 4*(y[0] -x) ))

# function for boundary condtions as y(a)=ya
def bc(ya,yb):
    return np.array([ya[0]-0,yb[0]-2])

x_ = np.linspace(0,1,20)                           # defining initial mesh with 20 points
y_s = np.zeros([2,len(x_)])                  # initializing the solution array       

y_s = solve_bvp(func,bc,x_,y_s)              # solving the differential equation
x = np.linspace(0,1,100)
sol= y_s.sol(x)[0]
plt.plot(x,sol,'g',label='numercal solution')

# plotting of exact function
e=np.exp(1)**2
ext = (e/(e*e -1))*2*np.sinh(2*x) + x
plt.plot(x,ext,'r.',label='analytical solution')

# exct solution
def exact(x):
    e=np.exp(1)**2
    return  ( (e/(e*e -1))*2*np.sinh(2*x) + x )

# percentage error array
err_arr=[]
for i in range(len(x)):
    err= np.absolute(y_s.sol(x[i])-exact(x[i])) / (exact(x[i]))
    err_arr.append(err*100)

print('percentage error at each step;',err_arr)

plt.xlabel('x')
plt.ylabel('y')
plt.title('solution of differential equation')
plt.legend()
plt.show()
