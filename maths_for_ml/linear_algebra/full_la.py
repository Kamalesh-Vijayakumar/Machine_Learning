import numpy as np 


a = np.array(
            [[1,2],
            [3,4]]
            )

#eigen decomposition
print(np.linalg.eig(a))

#determinant
print(np.linalg.det(a))

