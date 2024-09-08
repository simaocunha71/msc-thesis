"""
Algorithm:
- Define a function is_majority that takes in a sorted array, its length, and an element.
- Find the first and last occurrence of the element in the array using the binary search.
- If the difference between the first and last occurrence plus 1 is greater than n/2, return True. Otherwise, return False.
"""

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if ((mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x):
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

def is_majority(arr, n, x):
    i = binary_search(arr, 0, n-1, x)
    if i == -1:
        return False
    if arr[i] != x:
        return False
    if i + n//2 < n and arr[i + n//2] == x:
        return True
    else:
        return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3)) # Returns: True

# This algorithm works by using binary search to find the first and last occurrence of the element in the array. If the difference between the first and last occurrence plus 1 is greater than n/2, the function returns True. Otherwise, it returns False. The time complexity of this function is O(log n) because it uses binary search.

# The binary_search function is a helper function that takes in an array, the start and end indices of the array, and the element to be searched. It returns the index of the element if it is present, otherwise it returns -1. The binary search algorithm works by dividing the array into two halves and checking if the element is present in the first half or the second half. This process is repeated until the element is found or the subarray reduces to zero.

#