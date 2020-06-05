# Author : koshvendra Singh
# Date   : 05/06/2020
# Email  : koshvendra.singh@tifr.res.in

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

# generating 1024 uniformly distributed random numbers in [0,1)
num=1024
rand=np.random.rand(num)

# plotting these random numbers
x=np.arange(0,num,1)
plt.scatter(x,rand,s=0.3,c='red')
plt.xlabel('iteration for rand. no')
plt.ylabel('random number')
plt.title('uniformly distributed random no.')
#plt.legend()
plt.show()

#power spectrum of rand array
dx=x[1]-x[0]
Ft_rand=np.fft.fft(rand,norm='ortho')         # fourier transform of rand

# fixing factors in fourier transform
freq= np.fft.fftfreq(num,dx)
freq=2*np.pi*freq
factor=np.exp(-1j*freq*x[0])

# fixed fourier transform
Ft_rand=dx*np.sqrt(num/(2*np.pi))*factor*Ft_rand
Ft_rand=np.fft.fftshift(Ft_rand)
freq=np.fft.fftshift(freq)

pow_spect=(np.absolute(Ft_rand))**2       # power spectrum

# minimum and maximum wavevector

k_max=max(freq)                # maximum k vector
k_min=min(freq)                # minimum k vector

no_bin=5
dk_bin= (k_max-k_min )/(no_bin)           # length of each bin

# binned power spectrum and plotting 
bin_mean,bin_edges,binnumber=sc.binned_statistic(freq,pow_spect,statistic='mean',bins=5)

bin_ed=[]
for i in range(len(bin_edges)-1):
    l=(bin_edges[i+1]+bin_edges[i])/2
    bin_ed.append(l)

plt.bar(bin_ed,bin_mean,width=(bin_edges[1]-bin_edges[0]))
plt.xlabel('frequency')
plt.ylabel('binned power spectrum')
plt.show()
