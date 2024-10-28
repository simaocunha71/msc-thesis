"""
def find_first_occurrence(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            right = mid - 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return left if left < len(arr) and arr[left] == num else -1
"""
