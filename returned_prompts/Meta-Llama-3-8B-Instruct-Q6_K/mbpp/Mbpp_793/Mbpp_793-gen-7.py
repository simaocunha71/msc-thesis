```
def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```
The function `last` takes two parameters, `arr` which is the sorted array and `target` which is the element we are searching for. It iterates over the array in reverse order and returns the index of the last occurrence of the target element. If the target element is not found, it returns -1. 

The unit test `assert last([1,2,3],1) == 0` ensures that the function works correctly. It checks if the last position of 1 in the array [1,2,3] is 0, which is correct. 





