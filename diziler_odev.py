#Ödev 1
import numpy as np

sayi_dizisi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype="int")
print(sayi_dizisi.ndim)
print(sayi_dizisi.size)
#%%
#Ödev 2
import numpy as np
array2 = np.array([[1, 2, 6, 7], [4, 3, 9, 5]])
array3 = np.array([[[7, 5, 14], [21, 8, 11]], [[8, 6, 20], [14, 3, 9]]])
print(array2.ndim)
print(array3.ndim)

print(array2.size)
print(array3.size)

print(array2.shape)
print(array3.shape)
#%%
#Ödev 3
import numpy as np
array2 = np.array([[1, 2, 6, 7], [4, 3, 9, 5]])
array3 = np.array([[[7, 5, 14], [21, 8, 11]], [[8, 6, 20], [14, 3, 9]]])
print(array2[0][1])
print(array2[0][-1])
print(array3[-1][-1][-1])
print(array3[0][0][1])
#%%
#Ödev 4
import numpy as np
array2 = np.array([[1, 2, 6, 7], [4, 3, 9, 5]])
array3 = np.array([[[7, 5, 14], [21, 8, 11]], [[8, 6, 20], [14, 3, 9]]])
print(array2[0][1:3])
print(array2[1][1:])
print(array3[0][1][:])
print(array3[1][0][1:])
#%%
#Ödev 5
import numpy as np
zero = np.zeros((5, 3))
ones = np.ones((5, 3))
birlestirme = np.concatenate((zero, ones), axis=1)
print(birlestirme)