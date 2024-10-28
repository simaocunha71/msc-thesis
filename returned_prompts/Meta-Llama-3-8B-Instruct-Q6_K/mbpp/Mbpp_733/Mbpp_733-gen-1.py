```
def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            high = mid - 1
    return -1
```



In this code, we use a binary search algorithm to find the first occurrence of a given number in a sorted array. We start by initializing two pointers, `low` and `high`, to the start and end of the array, respectively. We then calculate the midpoint of the range `[low, high]` and compare the value at the midpoint to the target value.

If the value at the midpoint is less than the target, we know that the target must be in the right half of the range, so we set `low` to `mid + 1`. If the value at the midpoint is greater than the target, we know that the target must be in the left half of the range, so we set `high` to `mid - 1`.

If the value at the midpoint is equal to the target, we check if the target has been found for the first time. If it has, we return the midpoint index. If not, we set `high` to `mid - 1` to continue searching for the first occurrence of the target.

We continue this process until `low` is greater than `high`, at which point we return -1 to indicate that the target was not found in the array.

The unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` ensures that the function returns the correct index for the first occurrence of a given number in a sorted array.