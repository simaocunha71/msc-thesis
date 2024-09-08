from bisect import bisect_left
from bisect import bisect_right
def find_first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1