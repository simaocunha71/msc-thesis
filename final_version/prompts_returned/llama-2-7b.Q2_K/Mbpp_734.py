"""
Write a python function to find sum of products of all possible sublists of a given list. 
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
import math
def sum_Of_Subarray_Prod(arr):
    p = []
    for i in range (len(arr)):
        res = []
        for j in range (i+1, len(arr)):
            if arr[j] != 0:
                a = arr[:j]
                b= [x*y for x in a for y in arr[j:]][::-1] #print this to get better understanding of the solution.
                res += map(int,b)
        p.append(res[-1])
    return sum(p)+math.prod([-1]*len(arr)) 
        
    

if __name__ == '__main__':
    print sum_Of_Subarray_Prod([1,2,3])