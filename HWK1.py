# %% [markdown]
# # 2a and 2b

# %%
import numpy as np
# import numpy as np
import matplotlib.pyplot as plt
# import pylab as plt
from matplotlib import rcParams
# creating figure base features
rcParams['figure.figsize'] = (10,8)  # in inches
rcParams['font.size'] = 16

# creating random numbers then making them into vectors
vec_array = np.random.rand(300).reshape(100,3)
# print(vec_array) to ensure the array is correct
plt.title('Random X-Z Plane Vectors')
plt.xlabel('x-dimension')
plt.ylabel('z-dimension')
plt.scatter(vec_array[:,0],vec_array[:,2])
plt.show()

# %% [markdown]
# # 2c

# %%
def cart2cyl(x, y, z, array=True):
    
    r = np.sqrt(x**2 + y**2)
    #print(r)
    phi = np.arctan(y/x)
    #cyl = (r,phi,z)
    return r,phi,z
# test the function
# coords = cart2cyl(3, 4, 5)
# print(coords)
r,phi,z = cart2cyl(vec_array[:,0],vec_array[:,1],vec_array[:,2])
print(r)

# %% [markdown]
# # 2d

# %%
# calculating the mean/min/max using numpy package
rmean = np.mean(r)
rmin = np.min(r)
rmax = np.max(r)
print(rmin)
print(rmean)
print(rmax)





