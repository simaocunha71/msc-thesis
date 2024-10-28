```
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
``` 

The function `find_first_occurrence` takes a sorted array `arr` and a target number `target` as input. It returns the index of the first occurrence of `target` in `arr`. If `target` is not found in `arr`, it returns -1.

The function uses a binary search approach to find the first occurrence of `target`. It maintains two pointers, `left` and `right`, which initially point to the start and end of the array, respectively. It then calculates the middle index `mid` and compares the value of `arr[mid]` to `target`.

If `arr[mid]` equals `target`, the function checks if `mid` is 0 or if `arr[mid - 1]` is not equal to `target`. If either condition is true, it means that `mid` is the first occurrence of `target`, so the function returns `mid`. Otherwise, it updates `right` to `mid - 1` to continue searching in the left half of the array.

If `arr[mid]` is less than `target`, the function updates `left` to `mid + 1` to continue searching in the right half of the array. If `arr[mid]` is greater than `target`, the function updates `right` to `mid - 1` to continue searching in the left half of the array.

The function continues this process until `left` is greater than `right`, at which point it returns -1, indicating that `target` was not found in `arr`.