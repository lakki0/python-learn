# ---------------- pandas DataFrame -----------------

import pandas as pd

arr = pd.Series([10,20,30,40,50])
dt =  pd.DataFrame(arr)
dt.columns = ["list1"]
dt["list2"] = 25
dt["list3"] = dt["list1"]+dt["list2"]
# print(dt)

"""
   list1  list2  list3
0     10     25     35
1     20     25     45
2     30     25     55
3     40     25     65
4     50     25     75
"""
# del dt["list2"]
"""
   list1  list3
0     10     35
1     20     45
2     30     55
3     40     65
4     50     75
"""
dt.pop('list1')
print(dt)

# points = [89,93]
# name = ["lakki","yogi"]
# dic = {"Name":name,'Points':points}

# dt = pd.DataFrame(dic)
# print(dt)
"""
    Name  Points
0  lakki      89
1   yogi      93 
"""
    
# for row_value in dt.iterrows():
#     print("row values are : ",row_value)
    
"""row values are :  (0, Name      lakki      
Points       89
Name: 0, dtype: object)
row values are :  (1, Name      yogi       
Points      93
Name: 1, dtype: object)"""

# arr = pd.Series([10,20,30,40,50])
# dt =  pd.DataFrame(arr)
# print(dt)


# -----------------  pandas series -------------

# import pandas as pd
# import numpy as np

# arr = np.array([3.5,5.2,8.3,4.4,6.6])
# arr2 = pd.Series(arr)
# print(arr2.describe())
""" 
output is 
count    5.000000
mean     5.600000
std      1.890767
min      3.500000
25%      4.400000
50%      5.200000
75%      6.600000
max      8.300000
dtype: float64
"""


# arr = np.array([3.5,5.2,8.3,4.4,6.6])
# arr2 = pd.Series(arr)

# print('sorted values : \n',arr2.sort_values)
# print('mean values : \n',arr2.mean())
# print('max value : \n',arr2.max())
"""
sorted values : 
 <bound method Series.sort_values of 0    3.5
1    5.2
2    8.3
3    4.4
4    6.6
dtype: float64>
mean values :
 5.6
max value :
 8.3
 """

# index = ['a','b','c','d','e']
# index = ['a','b','c']   in that case rises the value error

# arr2 = pd.Series(arr,index=index)
# print(arr2)

# print('size of an array ',arr.size)

# arr = [3.5,5.2,8.3,4.4,6.6]
# arr2 = pd.Series(arr)
# arr3 = arr2+5
# print(arr3)

# arr = np.array([2,5,3,6,9,1,14,25])
# arr2 = pd.Series(arr)
# print(arr2)



