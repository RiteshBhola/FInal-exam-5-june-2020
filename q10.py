import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf  
pp=pf.PdfPages("q10_plots.pdf")   #All plots will be stored in this file

def sinc(x):
  if(x==0):
   return np.sqrt(2/np.pi)
  else:
   return (np.sin(x)/x)*np.sqrt(2/np.pi)
  
def Box(x):
  if(x>1):
    return 0
  elif(x<-1):
    return 0
  else:
    return(1)


x=np.linspace(-5,5,200,endpoint='True')
box=np.zeros(len(x))
for i in range(200):
  box[i]=Box(x[i])

plt.figure(figsize=(14,8))
plt.plot(x,box)
plt.title("Box Function",fontsize=15)
plt.xlabel("x",fontsize=15)
plt.ylabel("$f(x)$",fontsize=15)
pp.savefig()
    
def FT(n):
  xmax=25
  xmin=-25
  dx=(xmax-xmin)/(n-1)
  x= np.arange(xmin,xmax+dx,dx,dtype=np.complex_)



  data=np.zeros(n,dtype=np.complex_)
  analytic=np.zeros(n,dtype=np.complex_)
  k=np.fft.fftfreq(n,dx)
  k=2*np.pi*k
  kk=np.linspace(k.min(),k.max(),num=n,endpoint=True)
  for i in range(0,n,1):
    data[i]=Box(x[i])
    analytic[i]=sinc(kk[i])
    
  nft=np.fft.fft(data,norm='ortho')


  aft=dx*np.sqrt(n/(2.0*np.pi))*(np.exp(-1j*k*x.min()))*nft


  plt.figure(figsize=(14,8))
  plt.title("Fourier Transform of Box function, Sampling rate $\\Delta$ = %0.4f"%dx,fontsize=15)
  plt.plot(k,aft.real,"o",label="Fourier Transform using Numpy")
  plt.plot(kk.real,analytic.real,"",label="Analytic Fourier Transform")
  plt.legend(fontsize=15)
  plt.xlabel("k",fontsize=15)
  plt.ylabel("F(k)",fontsize=15)
  pp.savefig()
  

N=512
FT(N)
FT(2*N)
FT(4*N)
plt.show()
pp.close()
