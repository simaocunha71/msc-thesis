"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
from typing import Optional

def isUnique(arr: [int]|[float], n: int) -> bool :
    if len(set(arr)) == 1 and n == 0:
        return True
    else:
        return False

if __name__=='__main__':
    arr = [1,1,2,4]
    print(isUnique(arr, 3) )