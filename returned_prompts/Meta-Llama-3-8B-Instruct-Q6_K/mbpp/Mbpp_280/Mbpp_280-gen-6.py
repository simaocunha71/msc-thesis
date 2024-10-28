"""
You can use the sequential search algorithm, which iterates through the array until it finds the element or reaches the end of the array. Here is the Python solution:

```
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)
```

This function iterates through the array, comparing each element to the target element. If it finds a match, it returns a tuple with `True` and the index of the element. If it reaches the end of the array without finding the element, it returns a tuple with `False` and `-1`. The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` verifies the correctness of this solution. """


