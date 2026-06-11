import numpy as np
from scipy import stats

arr = np.array([10,20,30,40,60])

print(f"Mode {stats.mode(arr)}")