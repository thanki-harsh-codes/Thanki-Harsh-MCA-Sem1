import numpy as np
import pandas as pd

#1

a=np.array([-6,-7,-8,-9,-3,-4])
absolute_value=np.abs(a)
absolute_value

#2

b=np.array([5.7,6.4,7.6,3.8,8.7,9.3,2.1])
c=np.round(b)
c

#3

d=np.random.randint(2,11,(3,3))
d

#4

list=[9,8,7,6,5,4,3,2,1]
s=pd.Series(list)
s

array=np.array([6,8,7,9,4,5,3,2])
s2=pd.Series(array)
s2

dict={'a': 23, 'b':34, 'c':36, 'd':45, 'e':56}
s3=pd.Series(dict)
s3

#5

r=np.array([8,9,6,5,4,3,2,1])
s4=pd.DataFrame(r)
s4