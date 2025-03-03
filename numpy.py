import numpy as np
import sys
import time

size = 10**6  # 1 million

# python Lists
py_list = list(range(size))
py_size = sys.getsizeof(py_list)

# numpy array
np_array = np.arage(size)
np_size = np_array.nbytes

print(f"Python List Size: {py_size / 1024**2:.2f} MB")
print(f"NumPy Array Size: {np_size / 1024**2:.2f} MB")
