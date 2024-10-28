```
def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)
```


In this solution, we iterate over the array and check if the current element matches the given element. If it does, we return a tuple with `True` and the index of the element. If the element is not found after iterating over the entire array, we return a tuple with `False` and `-1` to indicate that the element was not found. The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` shows that the function should return the index of the element if it is found. If the element is not found, the function should return `-1`. 





This function uses a sequential search algorithm, which is simple but less efficient than other search algorithms like binary search for large arrays. It has a time complexity of O(n), where n is the length of the array. This means that the time it takes to search the array grows linearly with the size of the array.