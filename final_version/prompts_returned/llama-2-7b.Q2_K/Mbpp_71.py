"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
from typing import Optional

def comb_sort(arr: list) -> list:
	# print("Before Comb Sort, arr = ", arr[:])
    # print("\nCombination sort function.\n\n")
	if len(arr) < 2:
        return arr
    
	min_idx=0
	max_idx=len(arr)-1
	minval=0
	while min_idx<max_idx and max_idx>0 and arr[min_idx]<=arr[max_idx]:
	    if arr[min_idx]<arr[max_idx]:
            max_idx-=1
        else:
            min_idx+=1
    
	if minval==0:
		return comb_sort(arr[:min_idx]+list(arr[max_idx+1:]))+arr[min_idx:]
    else: # minval != 0
		return comb_sort(list(arr[:])+arr[:min_idx-1]+arr[max_idx+1:]}+arr[min_idx:]+arr[:max_idx+1]+arr[max_idx:-minval])
