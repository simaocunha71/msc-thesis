def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        min_diff = min(min_diff,diff)
    return min_diff

find_min_diff((1,5,3,19,18,25),6)












"""
This is a good question to practice the usage of for loop in Python. The idea is to sort the given array in ascending order. Then we initialize the minimum difference to infinity. After that we compare the consecutive elements in the sorted array to find the absolute difference and update the minimum difference if the difference we found is less than the current minimum difference. In the end we return the minimum difference.

The time complexity of this solution is O(nlogn) because of the sort function.
"""

"""
Correct Solution:

def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        min_diff = min(min_diff,diff)
    return min_diff

find_min_diff((1,5,3,19,18,25),6)
"""

"""
Incorrect Solution:

def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i])
        min_diff = min(min_diff,diff)
    return min_diff

find_min_diff((1,5,3,19,18,25),6)
"""

"""
Incorrect Solution:

def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+