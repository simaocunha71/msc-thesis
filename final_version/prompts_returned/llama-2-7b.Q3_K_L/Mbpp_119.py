"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(arr):
    count = 0
    if len(arr) >= 1:
        for i in range(1,len(arr)):
            if arr[i-1] != arr[i]:
                count += 1
    return count
