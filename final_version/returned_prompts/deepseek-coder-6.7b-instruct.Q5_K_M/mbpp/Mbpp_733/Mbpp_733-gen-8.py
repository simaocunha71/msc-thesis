def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 9) == 7
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 2) == 0
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6) == 4
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 8) == 6
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 10) == -1
"""

from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1