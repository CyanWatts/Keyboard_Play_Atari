import torch

'''
a = torch.rand(1,1)

print(type(a))
print(a)
'''
import numpy as np

a = np.random.randint(0,6,(1,1),dtype='int64')

print(type(a))
print(a)
a = torch.from_numpy(a)
print(type(a))
print(a)