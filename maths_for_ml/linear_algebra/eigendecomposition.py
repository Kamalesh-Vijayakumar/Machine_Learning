import numpy as np

#formua = 

D = np.array([[7, 3],
              [5, 9]])


eigenvectors,eigenvalues = np.linalg.eig(D)
#eigenvalues  =  np.linalg.eig(D)

print(eigenvalues)

print(eigenvectors)

