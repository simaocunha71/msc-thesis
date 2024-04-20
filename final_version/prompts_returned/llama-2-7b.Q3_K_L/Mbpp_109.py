"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
from typing import List, Optional

def odd_Equivalent(s:str,turns:int)->Optional[List]:
    """Write your implementation here"""
    if type(s) is not str or len(s)<2: return None
    res = []
    
    for i in s:
        if i.isdigit():
            res.append(i)
        
    res[0]=0
    res[1]=1
    list=res[:]
    for i in range(turns):
        if not list==[]:
            list=[list[0]+list[1],list[2]+list[3]]
        else:
            list=[1,0]
    
    n =len(list)
    res=[]
    for i in range(n-2):
        if  list[i].isdigit() and list[i+1].isalpha():
            res.append(int(list[i]))            
    return odd_Equivalent(s,turns)