```
def last(arr, element):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == element:
            return i
    return -1
```
This function iterates over the array in reverse order and returns the index of the last occurrence of the element. If the element is not found, it returns -1. The unit test `assert last([1,2,3],1) == 0` ensures that the function returns the correct index for the last occurrence of the element. 