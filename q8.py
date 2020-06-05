import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp 

h=0.01
x=np.arange(0,1+h,h)
n=x.size

def solution(x):
	return ((np.exp(2*x+2)-np.exp(-2*x+2))/(np.exp(4)-1))  + x
	
"Function"
def fun(x,y):
	 return np.vstack((y[1], 4*(y[0]-x)))


"Residuals of bondary condition"	 
def bc(ya, yb):
	return np.array([ya[0], yb[0]-2])
	
y=np.zeros((2,x.size))
y[0,0]=0
y[0,n-1]=2

sol = solve_bvp(fun, bc, x, y)
plt.subplot(1,2,1)
x_plot = np.linspace(0, 1, 100)
y_plot = sol.sol(x)[0]
plt.plot(x, y_plot,label="From scipy.integrate solve_bvp ")
plt.plot(x,solution(x),".m",label="Analytic Solution")
plt.xlabel("$x$",fontsize=22)
plt.ylabel("y(x)",fontsize=22)
plt.tick_params(labelsize=15)
plt.legend(fontsize=15)

plt.subplot(1,2,2)
x=np.arange(0+h,1+h,h)
error=np.abs(sol.sol(x)[0]-solution(x))/solution(x)
error*=100

plt.plot(x,error,".")
plt.xlabel("$x$",fontsize=22)
plt.ylabel("% Error(x)",fontsize=22)
plt.tick_params(labelsize=15)
plt.show()


outname="Ques8.txt" #Check this file for percentage error
A=np.zeros([x.size,2])
A[:,0]=x
A[:,1]=error
np.savetxt(outname,A)


