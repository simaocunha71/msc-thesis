"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""
import math
def max_Abs_Diff(arr):
    arr_len=len(arr)
    if arr_len==0:
        return max(math.fabs(arr[0]),math.fabs(arr[1]))
    else:
        diff_sum=0
        for i in range (2,arr_len):
            sub=abs(arr[i])-abs(arr[i-1])
            if abs(sub)==0 and len(arr)>2:
                diff_sum+=4.5
            else:
                diff_sum+=math.fabs(sub)
        return max(diff_sum,max_Abs_Diff(arr[:-1]))
        