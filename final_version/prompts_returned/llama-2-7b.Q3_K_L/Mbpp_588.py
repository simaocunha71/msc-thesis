"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""

def diff(l):
    if len(l) < 2: return 0;
    else:
        max = min = l[0] # Setup max and min of list
        for i in range(1,len(l)):
            if (max > l[i]) : max = l[i]
            elif (min < l[i]):  min = l[i]
        return abs(max - min)

print diff([5, 3.6, 2, 10, 34])