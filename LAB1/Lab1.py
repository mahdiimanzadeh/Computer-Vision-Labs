import numpy as np

A = np.random.rand(200,10)
B = np.zeros_like(A)

mu = np.zeros(A.shape[1])
for i in range(A.shape[0]):
  mu += A[i]
mu /= A.shape[0]

for i in range(A.shape[0]):
    B[i] = A[i] - mu

B
# The provided code computes a centered version of array A by subtracting the
#mean mu of each column from every element in the corresponding rows
B = A - np.mean(A, axis=0)
B
