```
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return (True, i)
    return (False, -1)
```


The problem is asking for a function that takes a list and an element as input, and returns a tuple. The first element of the tuple is a boolean indicating whether the element is in the list, and the second element is the index position of the element (or -1 if it's not found).

The problem seems to be asking for a sequential search, which is a simple and naive approach to find an element in a list. It works by iterating over the list and checking each element until it finds the target element.

Here's a Python function that implements this:

```
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return (True, i)
    return (False, -1)
```

This function iterates over the list using a for loop, and for each element, it checks if it's equal to the target element. If it finds the target element, it returns a tuple with a boolean indicating that the element is in the list, and the index position of the element. If it doesn't find the target element after iterating over the entire list, it returns a tuple with a boolean indicating that the element is not in the list, and -1 as the index position.

The unit test `assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)` ensures that the function works correctly. It checks that the function returns `(True, 3)` when searching for the element `31` in the list `[11,23,58,31,56,77,43,12,65,19]`. This is because `31` is indeed in the list at index position `3`. If the function returns anything else, the unit test will fail.