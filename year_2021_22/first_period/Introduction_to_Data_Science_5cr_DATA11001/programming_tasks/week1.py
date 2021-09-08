# Use this cell for your code
# Is it suppose to regular python list or can we use the numpy array. The regular python list causes a IOPub data
# rate exceeded error.
import numpy as np
from sklearn.datasets import load_boston
#========================CELL 1================================================
A = []
B = []
for i in range(10**7):
    A.append(i)
    B.append(i)
#========================CELL 2================================================
def add_with_for(A,B):
    C = []
    for i in A:
        sum = A[i] + B[i]
        C.append(sum)
    # add your code here
    return C
#========================CELL 3================================================
# define a new array using numpy
A = np.arange(10**7)
B = np.arange(10**7)
C = A + B
# Observations
# 1. The code was faster to run.
# 2. The code was more concised and elegant.
# 3. The print output was shorter than that of the regular python list.
#========================CELL 4================================================
a = np.arange(100).reshape(10,10)
a
#========================CELL 5============================================
a = np.resize([0.,1.], 100).reshape(10,10)
a
#========================CELL 6============================================
D = np.ones(100).reshape(10,10)
np.fill_diagonal(D, 0)
D
#========================CELL 7============================================
E = np.ones(100).reshape(10,10)
np.fill_diagonal(E, 0)
np.flip(E ,1)
#========================CELL 8============================================
np.round(np.linalg.det(D)*np.linalg.det(E))==np.round(np.linalg.det(D@E))
a = np.arange(9).reshape(3,3)
b = np.ones(9).reshape(3,3)
np.round(np.linalg.det(a)*np.linalg.det(b)) == np.round(np.linalg.det(a@b))
#========================CELL 9============================================
X, y = load_boston(return_X_y=True)
X.shape
#========================CELL 9============================================
np.where(X[:,0]>1)
