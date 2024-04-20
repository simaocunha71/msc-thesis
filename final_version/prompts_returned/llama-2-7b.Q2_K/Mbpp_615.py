"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""
from math import *
def average_tuple(tuple_list):
    assert len(tuple_list)>1 and type(tuple_list) == tuple

    # for each number in list
    for a in range(len(tuple_list)-1,0,-1):
        sum = 0.0
        average = 0
        for b in range (a+1,len(tuple_list)):
            sum += float(tuple_list[b][a])
            average+= tuple_list[b][a] / sum
        return average
\end{code}