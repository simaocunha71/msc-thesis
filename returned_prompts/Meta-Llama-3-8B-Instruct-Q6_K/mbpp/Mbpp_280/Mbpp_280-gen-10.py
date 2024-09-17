```
def sequential_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return (True, i)
    return (False, -1)
```



This function iterates over the array using the `enumerate` function to get both the index and the value of each element. If it finds the target element, it returns a tuple with `True` and the index. If it doesn't find the target element after iterating over the entire array, it returns a tuple with `False` and -1. This solution is based on the provided unit test, which checks if the function returns the correct result for a given array and target element. 

Note: This function has a time complexity of O(n), where n is the length of the array, because in the worst case it has to iterate over the entire array. This is because it is a sequential search, meaning it checks each element in the array one by one until it finds the target element or reaches the end of the array. 

However, for large arrays, this function may be slow. A more efficient solution would be to use a data structure that allows for faster lookup, such as a hash table or a binary search tree. 
```python
def sequential_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return (True, i)
    return (False, -1)
```


The unit test provided:
```
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
```


This test checks if the function returns the correct result for the given array and target element. It expects the function to return `(True, 3)` when searching for the element `31` in the array `[11,23,58,31,56,77,43,12,65,19]`. 
```python
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
```


This test ensures that the function is working correctly and returns the expected result for the given input. 
```python
assert sequential_search([11,23,58,31,56,77,43,12,65,19],99) == (False, -1)
```


This test checks if the function returns the correct result for the given array and target element