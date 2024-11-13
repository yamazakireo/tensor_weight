import numpy as np

M234 = np.array(range(1,25)).reshape(2,3,4)
v1 = np.array([1,1,1,1])
'''
answer = np.dot(M234,v1)

print(answer)

#[[10 26 42][58 74 90]]
'''

print(np.shape(np.sum(M234,axis=2)))