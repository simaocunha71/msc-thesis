```
def find_first_occurrence(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < num:
                return mid
            high = mid - 1
    return -1
```





The function `find_first_occurrence` takes a sorted array `arr` and a number `num` as input. It returns the index of the first occurrence of `num` in `arr`. If `num` is not found in `arr`, it returns `-1`.

The function uses a binary search approach to find the first occurrence of `num` in `arr`. It maintains two pointers, `low` and `high`, which represent the range of the array that still needs to be searched. Initially, `low` is set to `0` and `high` is set to the length of `arr` minus `1`.

The function enters a loop that continues until `low` is greater than `high`. In each iteration, it calculates the midpoint `mid` of the range `low` to `high`. If `arr[mid]` is less than `num`, it updates `low` to `mid + 1`. If `arr[mid]` is greater than `num`, it updates `high` to `mid - 1`. If `arr[mid]` is equal to `num`, it checks if `mid` is `0` or if `arr[mid - 1]` is less than `num`. If either condition is true, it returns `mid` as the index of the first occurrence of `num`. If `mid` is not the first occurrence of `num`, it updates `high` to `mid - 1` to continue searching for the first occurrence.

If the loop completes without finding the first occurrence of `num`, the function returns `-1`. This indicates that `num` is not present in `arr`.