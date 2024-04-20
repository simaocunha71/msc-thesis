"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
import bisect
def kth_element(arr, k):
    # create a sentinel to mark the end of the array at index len - 1:
    s = arr[-1] if isinstance(arr,-1) else len(arr) - 1
    return bisect.bisect_left(arr[:s], k,True,lambda i,l,k:i+1<len(arr)-k and l or lambda :(l-1,True))[0]