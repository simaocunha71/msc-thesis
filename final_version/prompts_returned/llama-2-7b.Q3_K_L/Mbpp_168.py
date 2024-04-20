"""
Write a function to count the number of occurrences of a number in a given list.
assert frequency([1,2,3], 4) == 0
"""

def frequency(lst, num):
    if not isinstance(lst[0] , int):
        lst = [num for i in lst for j in lst]
    ret = []
    for i in lst:
        if i == num:
            ret.append(1)
        else:
            ret.append(ret[-1] + 1)
            
    return sum(ret)