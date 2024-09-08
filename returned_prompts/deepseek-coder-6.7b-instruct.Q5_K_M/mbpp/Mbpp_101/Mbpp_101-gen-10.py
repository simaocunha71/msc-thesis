def kth_element(arr, k):
    arr.sort()
    return arr[k-1]
"""
Here we are sorting the array in ascending order and then returning the kth element which is at index k-1 because the array is 1-based indexed.
"""

