```
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return (True, i)
    return (False, -1)
```
The provided unit test suggests that the function should return a tuple containing a boolean indicating whether the element is in the array and the index position of the element (or -1 if the element is not found). 

The provided unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` implies that the function should return `(True, 3)` when the target element `31` is in the array, and `(False, -1)` when the target element is not in the array. 

This function uses a sequential search approach, where it iterates through the array and checks each element until it finds the target element or reaches the end of the array. If the target element is found, it returns a tuple with `True` and the index position of the element. If the target element is not found, it returns a tuple with `False` and `-1`.  The function is case-sensitive and will not work correctly if the array contains duplicate elements.  For a more robust solution, you might want to consider using a hash table or a binary search algorithm. 