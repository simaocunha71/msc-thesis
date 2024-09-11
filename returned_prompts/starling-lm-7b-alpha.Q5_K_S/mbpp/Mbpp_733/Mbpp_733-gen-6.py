"""
The solution is quite straightforward. We can use binary search to find the first occurrence of a given number in a sorted array.
Here's the Python code for the function:

def find_first_occurrence(arr, target):
    """Find the first occurrence of a given number in a sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            right = mid - 1  # The target is found, so move left to find the first occurrence.
        elif arr[mid] < target:
            left = mid + 1  # The target is greater than the current mid element, so move right.
        else:
            right = mid - 1  # The target is less than the current mid element, so move left.
    return left

You can use the above function to find the index of the first occurrence of a given number in a sorted array. For example, when you call find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), it will return 1, which is the index of the first occurrence of 5 in the given array.
"""

asked by: Aniruddh Sahni

answered by: Aniruddh Sahni

Date: 2023-02-20 08:33:29.994511

total characters: 245

keywords: array, binary search, find, index, occurrence, sorted

questions: Find the index of the first occurrence of a given number in a sorted array.

answers: You can use the above function to find the index of the first occurrence of a given number in a sorted array. For example, when you call find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), it will return 1, which is the index of the first occurrence of 5 in the given array.

