```
def last(arr, target):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == target:
            return i
    return -1
```





This function iterates over the array in reverse order and returns the index of the last occurrence of the target element. If the target element is not found, it returns -1. The unit test `assert last([1,2,3],1) == 0` ensures that the function returns the correct index for the last occurrence of the target element.

Note: The problem statement does not explicitly state whether the array is sorted or not. However, based on the unit test, we can assume that the array is sorted. If the array is not sorted, the function may not work correctly.