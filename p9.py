# Author : koshvendra Singh
# date : 05/06/2020
# description : calculating singular values of matrix

import numpy as np

# for first matrix
mat_1= np.array([[2,1],[1,0],[0,1]])

# calculating  SVD by numpy function
[u_1,s_1,vh_1]=np.linalg.svd(mat_1)

# singular values, s_1
sing_1 = np.zeros(np.shape(mat_1))
for i in range(len(s_1)):                  
    sing_1[i,i]=s_1[i]

print('unitary matrix,U_1 :',u_1)
print('diagonal contains the singular values of mat_1',sing_1)            
print('Vh=',vh_1)
print('reconstruction of matrix mat_1 :',np.matmul(u_1,np.matmul(sing_1,vh_1)))

mat_2=np.array([[1,1,0],[1,0,1],[0,1,1]])

[u_2,s_2,vh_2]=np.linalg.svd(mat_2)

sing_2=np.zeros(np.shape(mat_2))
for i in range(len(s_2)):
    sing_2[i,i]=s_2[i]

print('unitary matrix,U_2 :',u_2)
print('diagonal contains the singular values of mat_2',sing_2)           
print('Vh=',vh_2)
print('reconstruction of matrix mat_2 :',np.matmul(u_2,np.matmul(sing_2,vh_2)))


