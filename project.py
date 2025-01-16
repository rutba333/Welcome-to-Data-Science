import numpy as np

A=np.arange(9,dtype=float).reshape(3,3)
print("First array (A) is : ")
print(A)
('\n')
B=np.array([10,10,10])
print("second array (B) is: ")
print(B)
print('\n')


#addition
print("The addition of array A and Bis:")
print(np.add(A,B))
('\n')

#substraction
print("The substraction of A and Bis :")
print(np.subtract(A,B))
('\n')

#multiplication
print("The multiplication of A and B is :")
print(np.multiply(A,B))
('\n')

#division
print("The division of A and B is:")
print(np.divide(A,B))
('\n')
