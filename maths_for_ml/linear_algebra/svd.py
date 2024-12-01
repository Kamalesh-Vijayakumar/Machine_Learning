import numpy as np

# Original matrix
A = np.array([[3, 2],
              [2, 3]])

# Perform SVD
U, Sigma, VT = np.linalg.svd(A)

# Reconstruct the matrix
Sigma_matrix = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(Sigma_matrix, Sigma)

A_reconstructed = U @ Sigma_matrix @ VT

print("Original Matrix:\n", A)
print("U Matrix:\n", U)
print("Singular Values:\n", Sigma)
print("V Transpose Matrix:\n", VT)
print("Reconstructed Matrix:\n", A_reconstructed)
