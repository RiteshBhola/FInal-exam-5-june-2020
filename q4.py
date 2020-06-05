import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf  
pp=pf.PdfPages("q4_plots.pdf")
n=1024
a=np.random.rand(n)

plt.figure(figsize=(14,8))
plt.plot(a,label="Uniformy generated random numbers")
plt.legend(fontsize=17)
plt.xlabel("$x_p$",fontsize=15)
plt.ylabel("f($x_p$)",fontsize=15)

dft=np.fft.fft(a,norm='ortho')
k=np.fft.fftfreq(n)
ii=np.argsort(k)
power=dft*np.conj(dft)
power=power/n
pp.savefig()

plt.figure(figsize=(14,8))
plt.plot(k[ii],power[ii].real,"-")
plt.plot(k,power.real,".",label="power sprectrum")
plt.legend(fontsize=17)
plt.xlabel("$k$",fontsize=15)
plt.ylabel("$P(k)$",fontsize=15)
pp.savefig()
print("k max is ",k.max())
print("k min is ",k.min(),"with n= %d"%(n))

bins=5
bw=int(n/5)
binned_pow=np.zeros(bw,dtype='complex_')


for kk in range(bw):
  for i in range(bins):
    binned_pow[kk]+=power[kk+i*bw]
  binned_pow[kk]=binned_pow[kk]/bins

plt.figure(figsize=(14,8))
bb=np.fft.fftfreq(bw)
ii=np.argsort(bb)
plt.plot(bb[ii],binned_pow[ii].real,"-*",label="Binned power spectrum")
plt.legend(fontsize=17)
plt.xlabel("k",fontsize=15)
plt.ylabel("$P_{binned}(k)$",fontsize=15)
pp.savefig()
plt.show()
pp.close()



