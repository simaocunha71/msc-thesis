"""
Write a python function to find the index of smallest triangular number with n digits. 
assert find_Index(2) == 4
"""
from math import log10, ceil
def find_Index(n):   
    if n <= 0 : return -1
  
    d = [pow(10,i), for i in range(int(log10(n)),-1,-1j)]
  
    index = 3+len(d[-1])
    while index >= len(d):
        if not d[index].isdigit():
            return -1
        
    f=d[index]
    for j in range(2,int(log10(n))-2,-1j):
        tmp = f*pow(10,j)
        if (tmp < n):
            index -= 3 + len((str)(ceil(tmp)))
  
    return index
