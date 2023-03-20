import numpy as np
import pandas as pd

arr = np.random.rand(3)
print('Arr: ', arr)


s1 = pd.Series(arr, index=['a', 'b', 'c'])
print('S1: \n', s1)
print('at 1: ', s1[1])

print(s1.index)

a2d = np.random.rand(3, 2)
print('ad: \n', a2d)

df = pd.DataFrame(a2d)
print('D_frame: \n', df)

print('df.columns: \n', df.columns)
print(type(df[0]))
