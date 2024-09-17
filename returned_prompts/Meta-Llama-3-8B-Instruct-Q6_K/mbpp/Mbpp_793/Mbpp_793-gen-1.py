```
def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```
This function iterates through the array from right to left (from the end of the array to the beginning). It stops when it finds the target element, or when it reaches the beginning of the array. If it doesn't find the target element, it returns -1. The unit test `assert last([1,2,3],1) == 0` shows that the function should return the index of the last occurrence of the target element. If the target element is not found, it returns -1. 







