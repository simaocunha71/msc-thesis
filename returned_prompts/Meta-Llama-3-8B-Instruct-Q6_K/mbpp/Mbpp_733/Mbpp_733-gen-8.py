```
def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```


The function `find_first_occurrence` takes a sorted array `arr` and a target number `target` as inputs. It returns the index of the first occurrence of `target` in the array. If `target` is not found in the array, it returns -1.

The function uses a binary search algorithm to find the target in the array. It maintains two pointers, `low` and `high`, which represent the current search range in the array. The search range is initially set to the entire array.

In each iteration, the function calculates the midpoint `mid` of the search range and compares the value of the element at `mid` with the target. If the value at `mid` is equal to the target, the function checks whether the element at `mid - 1` is less than the target. If it is, the function returns `mid` as the index of the first occurrence of the target. Otherwise, the function updates the search range to the left half of the array.

If the value at `mid` is less than the target, the function updates the search range to the right half of the array. If the value at `mid` is greater than the target, the function updates the search range to the left half of the array.

The function continues this process until the search range is empty, in which case it returns -1 to indicate that the target is not found in the array.

The unit test `assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1` ensures that the function returns the correct index of the first occurrence of the target number in the array.