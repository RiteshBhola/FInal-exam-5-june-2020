import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt

seed=1
a=1664525
c=1013904223
m=4294967296
x=seed

n=100000
res=[]
for i in range(n):
  x=(a*x + c)%m
  res.append(x)
  
plt.plot(res,"o")

flag=0
for i in range(n):
  if res[i]==seed:
    flag+=1
    
if(flag==0):
  print("seed not present")
else:
  print("seed present")
  
plt.show()



