import numpy as np

t = np.array([0., 1., 2., 3., 4., 5., 6.])
print(t)
print("Rank of t: ", t.ndim)
print("Shape of t: ", t.shape)

import torch
t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
print(t)
print(t.dim())
print(t.shape)
print(t.size())