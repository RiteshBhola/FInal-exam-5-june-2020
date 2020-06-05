import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt
print(
"""
SVD of A=
| 2 1 |
| 1 0 |
| 0 1 |
""")
m,n=3,2
A=np.array([2,1,1,0,0,1]).reshape(m,n)
u, s, vh = np.linalg.svd(A, full_matrices=True)


smat = np.zeros((m, n))

smat[:n, :n] = np.diag(s)
	
print("Trans(V) is \n",vh)
print("U is \n",u)
print("S is \n",smat)
print("U.S.Trans(V)\n",u@smat@vh)
print()
print()
print("No.of singular values:",len(s))
print("Singular Values are:",s)
print(
"""
*********************************************
*********************************************
SVD of A=
 
| 1 1 0 |
| 1 0 1 |
| 0 1 1 |
""")
m,n=3,3
A=np.array([1,1,0,1,0,1,0,1,1]).reshape(m,n)
u, s, vh = np.linalg.svd(A, full_matrices=True)


smat = np.zeros((m, n))

smat[:n, :n] = np.diag(s)
	
print("Trans(V) is \n",vh)
print("U is \n",u)
print("S is \n",smat)
print("U.S.Trans(V)\n",u@smat@vh)
print()
print()
print("No.of singular values:",len(s))
print("Singular Values are:",s)
