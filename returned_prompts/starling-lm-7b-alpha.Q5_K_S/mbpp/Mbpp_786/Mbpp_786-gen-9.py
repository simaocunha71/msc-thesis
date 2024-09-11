def right_insertion(arr, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left if arr[left] < val else right


# Test Cases
print(right_insertion([1,2,4,5], 3))  # 3
print(right_insertion([1,2,4,5], 6))  # 4
print(right_insertion([1,2,4,5], 0))  # 0
print(right_insertion([1,2,4,5], 7))  # 4
print(right_insertion([1,2,4,5], 8))  # 5
print(right_insertion([], 0))  # 0
print(right_insertion([1], 0))  # 0

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""


def binary_search(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return -1 if left > right else mid


# Test Cases
print(binary_search([1,2,4,5], 3))  # 3
print(binary_search([1,2,4,5], 6))  # 4
print(binary_search([1,2,4,5], 0))  # -1
print(binary_search([1,2,4,5], 7))  # 4
print(binary_search([1,2,4,5], 8