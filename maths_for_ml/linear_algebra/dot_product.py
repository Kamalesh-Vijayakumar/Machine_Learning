#USING PYTHON 
vector_u = [1, 2, 3]
vector_v = [4, 5, 6]
k =[]
for i,v in zip(vector_u,vector_v):
    k.append(i*v)
print(sum(k))


#USING NUMPY 
import numpy as np
vector_u = np.array([1, 2, 3])
vector_v = np.array([4, 5, 6])
result = np.dot(vector_u, vector_v)
print("Dot Product (NumPy):", result)


#for COSINE SIMILARITY

#Combines dot product and magnitudes to give a normalized similarity score.

import numpy as np
vector_u = np.array([1, 2, 3])
vector_v = np.array([4, 5, 6])
result = np.dot(vector_u, vector_v)

#Compute dot product geometrically
magnitude_u = np.linalg.norm(vector_u)  # ||u||
magnitude_v = np.linalg.norm(vector_v)  # ||v||

# Angle (cosine) between the vectors
cos_theta = result / (magnitude_u * magnitude_v)
print("Cosine of the Angle:", cos_theta)



 
#VISUALIZING THE VECTORS  
import numpy as np
vector_u = np.array([1,2,3])
vector_v = np.array([2,2,3])
import matplotlib.pyplot as plt

# Plot vectors
origin = [0, 0]
plt.quiver(*origin, vector_u[0], vector_u[1], color='r', scale=1, scale_units='xy', angles='xy', label='Vector U')
plt.quiver(*origin, vector_v[0], vector_v[1], color='b', scale=1, scale_units='xy', angles='xy', label='Vector V')

plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()
