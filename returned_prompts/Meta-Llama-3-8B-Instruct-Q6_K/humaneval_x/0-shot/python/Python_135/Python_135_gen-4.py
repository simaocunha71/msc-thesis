```
def can_arrange(arr):
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            return i-1
    return -1
```


Explanation:
The function iterates over the array starting from the second element (index 1). For each element, it checks if it is greater than the previous element. If it finds such an element, it returns the index of the previous element, which is the largest index of an element not greater than or equal to the element preceding it. If no such element is found after iterating over the entire array, the function returns -1. The given array will not contain duplicate values, so there is no need to handle duplicate values in the function.