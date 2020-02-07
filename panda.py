import pandas as  pd
import numpy as np
s=pd.Series([2,34,4,5,6],index=['a','b','c','d','e'])
print(s)
print(type(s))
t=pd.Series(np.array(range(0,10))**2,index=range(0,10))
print(t)
u=np.array(range(0,10))**2
print(u)
