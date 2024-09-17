```
def last(array, target):
    for i in range(len(array) - 1, -1, -1):
        if array[i] == target:
            return i
    return -1
```
This function iterates over the array from the end to the beginning, and returns the index of the last occurrence of the target element. If the target element is not found, it returns -1. The unit test `assert last([1,2,3],1) == 0` ensures that the function works correctly.