import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt


a=1664525
c=1013904223
m=429496
seed=m/2
x=seed

n=20000
res=[]
for i in range(n):
  x=(a*x + c)%m
  res.append(x)

res=np.array(res)  
plt.plot(res,"o")


flag=0
for i in range(n):
  if res[i]==seed:
    flag+=1
    
if(flag==0):
  print("seed not present")
else:
  print("seed present and appears",flag,"times")
plt.show()



