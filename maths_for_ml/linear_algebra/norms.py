import numpy as np

# Define the vector
v = np.array([3, -4])

# L1 Norm (Manhattan Norm)
l1_norm = np.sum(np.abs(v))
print(f"L1 Norm: {l1_norm}")

# L2 Norm (Euclidean Norm)
l2_norm = np.linalg.norm(v)  # or np.sqrt(np.sum(v**2))
print(f"L2 Norm: {l2_norm}")

# L∞ Norm (Max Norm)
l_inf_norm = np.max(np.abs(v))
print(f"L∞ Norm: {l_inf_norm}")
