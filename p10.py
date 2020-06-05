# Author : Koshvendra Singh
# Date   : 05/06/2020
# Description : fourer transform of box function

import numpy as np
import matplotlib.pyplot as plt

# definig box function
def box_func(x):
    if np.absolute(x)<1:
        return (1)
    else:
        return(0)
    

# plotting box function
x=np.linspace(-10,10,100)
y=[]
for i in range(len(x)):
    y.append(box_func(x[i]))

plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('box function')
plt.show()


for i in range(3):
    num=2**(8+i)               # for different sampling rates
    t=np.linspace(-30,30,num)
    dt=t[1]-t[0]               # reolution in position space
    box=[]
    for i in range(len(t)):
        box.append(box_func(t[i]))
        
    ft_box=np.fft.fft(box,norm='ortho')
    freq=2*np.pi*np.fft.fftfreq(len(t),dt)
    factor=np.exp(-1j*freq*t[0])
    ft_box=dt*np.sqrt(len(t)/(2*np.pi))*factor*ft_box

    freq=np.fft.fftshift(freq)              # shifted frequency
    ft_box=np.fft.fftshift(ft_box)          # shifted fourier transform
    
    # plotting
    plt.plot(freq,np.real(ft_box))
    plt.xlabel('freq')
    plt.ylabel('FT of box function')
    plt.show()
