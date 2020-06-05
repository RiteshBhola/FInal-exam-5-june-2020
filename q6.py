import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
	return 32*y+66*z+(2/3)*x + (2/3)
	
def g(x,y,z):
	return -66*y - 133*z -(1/3)*x -(1/3)



def real_f(t):
	return (-np.exp(-100*t)+2*np.exp(-t)+2*t)/3
	
def real_g(t):
	return (2*np.exp(-100*t)-np.exp(-t)-t)/3

	
dx=0.01
x=np.arange(0,0.5+dx,dx)	
n=x.size


y=np.zeros(n)
z=np.zeros(n)

y[0]=1/3
z[0]=1/3

for i in range(0,n-1,1):
	k0=dx*f(x[i],y[i],z[i])
	l0=dx*g(x[i],y[i],z[i])
	
	k1=dx*f(x[i]+dx/2,y[i]+k0/2,z[i]+l0/2)
	l1=dx*g(x[i]+dx/2,y[i]+k0/2,z[i]+l0/2)

	k2=dx*f(x[i]+dx/2,y[i]+k1/2,z[i]+l1/2)
	l2=dx*g(x[i]+dx/2,y[i]+k1/2,z[i]+l1/2)

	k3=dx*f(x[i]+dx/2,y[i]+k2,z[i]+l2)
	l3=dx*g(x[i]+dx/2,y[i]+k2,z[i]+l2)

	y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
	z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6

	
plt.figure(figsize=(12,8))
plt.plot(x,y,".-",label="y1(x)")
plt.plot(x,z,".-",label="y2(x)")
plt.plot(x,real_f(x),"-",label="analytic y1(x)")
plt.plot(x,real_g(x),"-",label="analytic y2(x)")

plt.xlabel("$x$",fontsize=20)
plt.ylabel("$f(x)$",fontsize=20)
plt.tick_params(labelsize=15)
plt.legend(fontsize=15)
plt.savefig("q6plot.pdf")

plt.figure(figsize=(10,6))
plt.plot(x,np.abs(real_f(x)-y),"D",label="absolute error y1(x)")
plt.plot(x,np.abs(real_g(x)-z),"^",label="absolute error y2(x)")

plt.xlabel("$x$",fontsize=20)
plt.ylabel("$f(x)$",fontsize=20)
plt.tick_params(labelsize=15)
plt.legend(fontsize=15)
plt.savefig("q6plot_errors.pdf")
plt.show()

print("""Analytic solution obtained from wolfram alpha matches with 
numerical solution (within error).
"""
)



