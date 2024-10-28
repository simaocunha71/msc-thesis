```
def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```


The problem is asking to find the last position of a target element in a sorted array. The function should return the index of the last occurrence of the target element if it exists in the array, otherwise, it should return -1.

The given unit test `assert last([1,2,3],1) == 0` suggests that the function should return the index of the last occurrence of the target element (1 in this case) which is 0.

Here is a python function that solves the problem:
```
def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```
This function iterates over the array in reverse order and returns the index of the target element if it is found. If the target element is not found, it returns -1. The unit test `assert last([1,2,3],1) == 0` passes with this function.