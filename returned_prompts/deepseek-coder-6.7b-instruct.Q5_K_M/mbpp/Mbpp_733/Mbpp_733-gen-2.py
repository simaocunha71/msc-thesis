def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left if left < len(arr) and arr[left] == target else -1

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))  # 1

# Find the first occurrence of a given number in a sorted array
# Given an array of integers sorted in ascending order, find the first occurrence of a given target number. Your algorithm should have logarithmic time complexity. 
# Return -1 if the target number is not found in the array.

# Hint: This problem is a variation of Binary Search. What makes this problem different from regular binary search is that we don't stop the search as soon as we find the target element, we continue to search towards the left of the array to see if there are any other occurrences of the target number.

# Solution
# We can use a modified version of Binary Search where we first find the target element and then continue to search towards the left of the array to see if there are any other occurrences of the target number.

# If we find the target, we have two options:
# 1. If the middle element is not the first occurrence of the target (i.e., arr[mid-1] is not equal to target), we return mid.
# 2. If the middle element is the first occurrence of the target, we update our right pointer to mid - 1 to continue the search towards the left of the array.

# If we don't find the target, we return -1.

# This solution has a time complexity of O(log n) because we are using Binary Search, and it has a space complexity of O(1) since we are not using any additional space that scales with the input size.

# Here is the Python code for the solution:

# def find_first_occurrence(arr, target