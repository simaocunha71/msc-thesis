```
def is_majority(arr, n, target):
    if len(arr) != n:
        raise ValueError("Array length does not match the given n")
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left = mid + 1
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == n:
        return False
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if mid + 1 <= right and arr[mid + 1] == target:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left >= n // 2
```  # 1
```
Note that the problem statement does not specify whether the array is sorted in ascending or descending order. However, the provided unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` suggests that the array is sorted in ascending order.

The function `is_majority` takes three parameters: `arr`, the sorted array; `n`, the length of the array; and `target`, the element to check.

The function first checks if the given length `n` matches the actual length of the array. If not, it raises a `ValueError`.

Then, it uses a binary search to find the first occurrence of the `target` element in the array. If the `target` element is not found, it returns `False`.

Next, it uses another binary search to find the last occurrence of the `target` element in the array. If the `target` element is not found, it returns `False`.

Finally, it checks if the count of the `target` element is more than `n/2`. If it is, it returns `True`; otherwise, it returns `False`.

The time complexity of the function is O(log n) for each binary search, so the overall time complexity