def kth_element(arr, k):
    arr.sort()
    return arr[k-1]
"""
The function works by sorting the array in ascending order, then returning the kth element of the sorted array.
"""

# OR

def kth_element(arr, k):
    arr.sort()
    return arr[-k]
"""
The function works by sorting the array in ascending order, then returning the kth element from the end of the sorted array.
"""

# OR

def kth_element(arr, k):
    return sorted(arr)[k-1]
"""
The function works by sorting the array in ascending order and returning the kth element of the sorted array.
"""

# OR

def kth_element(arr, k):
    return sorted(arr)[-k]
"""
The function works by sorting the array in ascending order and returning the kth element from the end of the sorted array.
"""

# OR

def kth_element(arr, k):
    return heapq.nlargest(k, arr)[-1]
"""
The function works by using the nlargest function from the heapq module to find the kth largest element in the array, then returning this element.
"""

# OR

def kth_element(arr, k):
    return heapq.nsmallest(len(arr) - k + 1, arr)[-1]
"""
The function works by using the nsmallest function from the heapq module to find the kth smallest element in the array, then returning this element.
"""

# OR

def kth_element(arr, k):
    return sorted(arr)[k-1]
"""
The function works by sorting the array in ascending order and returning the kth element of the sorted array.
"""

# OR

def kth_element(arr, k):
    return sorted(arr)[-k]
"""
The function works by sorting the array in ascending order and returning the kth element from the end of the sorted array.
"""

# OR

def kth_element(arr, k):
    return heapq.nsmallest(k,