```
def last(arr, target):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1
```
This function iterates through the array from the end to the start, checking each element to see if it matches the target. If it finds a match, it returns the index of that element. If it doesn't find a match, it returns -1. 

The unit test `assert last([1,2,3],1) == 0` ensures that the function returns the correct index for the last occurrence of the element. 

Note that this function assumes that the array is sorted in ascending order. If the array is not sorted, or if the element is not found, the function may not work correctly. 





