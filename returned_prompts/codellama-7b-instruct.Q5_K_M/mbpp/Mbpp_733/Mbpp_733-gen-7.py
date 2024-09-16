"""
def find_first_occurrence(arr, num):
    # Time complexity: O(log n)
    # Space complexity: O(1)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1
"""