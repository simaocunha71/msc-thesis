"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
from typing import Any, List

def dif_Square(n:int)->List[Any]:
    if n<0 : return []
    sum = list()
    s = 1
    for i in range (2, int((sqrt(n))+1)):
        d = sqrt(s**2)-s*i
        if abs(d) < 1e-9 and abs(sqrt(n)-d)<1e-9 : return []
        s+=i
    #print("Sum: ", sum, ", ", "abs(sum):", abs(sum))
    if ( sum[0] == sum[-1] or sum[0] == 0 and sum[-1]==s ) & ( sum[0] == 0 and sum[-1] != s or sum[0] != 0 and sum[-1] == sqrt(n)-d ):
        return ["yes"]
    else:
        #print("yes or no ", sum)
        if not ( sum[0]==sum[-1] or sum[0]==0 and sum[-1]=s or sum[0]!=0 and sum[-1] == sqrt(n)-d ):
            return ["no"]+[f"{abs(i)} for i in sum"]    
    else:return []
# [1, 2, 3] + [4, 5, 6] = 10
# 10 - (1+2+3) = 7
# or (7-1)-(7-2) = 4
