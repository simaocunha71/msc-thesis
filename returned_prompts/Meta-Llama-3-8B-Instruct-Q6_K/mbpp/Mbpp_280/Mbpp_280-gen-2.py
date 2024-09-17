```
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)
```


This function iterates over the array and checks each element to see if it matches the given element. If a match is found, it returns a tuple with a boolean value of True and the index of the element. If the element is not found after checking all elements, it returns a tuple with a boolean value of False and an index of -1.

The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` confirms that the function works correctly. It checks if the element 31 is in the array and returns the correct index (3) when it is found. If the element was not found, the function would return (False, -1). 







