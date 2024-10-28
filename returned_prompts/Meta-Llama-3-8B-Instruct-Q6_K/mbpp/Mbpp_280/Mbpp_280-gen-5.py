```
def sequential_search(arr, element):
    for i, val in enumerate(arr):
        if val == element:
            return (True, i)
    return (False, -1)
```


The function `sequential_search` takes a list `arr` and an element `element` as input. It iterates over the list using the `enumerate` function, which returns both the index and the value of each element. If the element is found, it returns a tuple containing `True` and the index of the element. If the element is not found, it returns a tuple containing `False` and `-1`. This function is used to search for an element in a list in a linear fashion. The time complexity of this function is O(n), where n is the number of elements in the list. It is not efficient for large lists, but it is simple and easy to understand. The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` ensures that the function is working correctly. It checks if the element `31` is in the list and returns the correct index `3`. If the element is not in the list, it returns `False` and `-1`. In this case, the element `31` is in the list, so the function returns `(True, 3)`. The function can be used in scenarios where a simple linear search is required. 





The unit test provided is:
```
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
```
This test checks if the function `sequential_search` correctly returns a tuple containing `True` and the index of the element `31` in the list. The expected output is `(True, 3)`, which means the element `31` is in the list at index `3`. If the function returns anything else, the test will fail. 





Here is the solution:
```
def sequential_search(arr, element):
    for i, val in enumerate(arr):
        if val == element:
            return (True, i)
    return (False, -1)
```





The function `sequential_search` takes a list `arr` and an element `element` as input. It iterates over the list using the `enumerate` function, which returns both the index and the value of each