You can use the built-in Python function `all()` to check if all elements in a list are equal to a given element. The `all()` function returns `True` if all elements of the iterable are true. If at least one element is false, it returns `False`.

Here is a Python function that uses the `all()` function to check if all items in a list are equal to a given element:

```
def check_element(lst, element):
    return all(item == element for item in lst)
```

This function works by iterating over each item in the list and checking if it is equal to the given element. If any item is not equal to the element, the `all()` function returns `False`. If all items are equal to the element, the `all()` function returns `True`. 

This function passes the given unit test:

```
assert check_element(["green", "orange", "black", "white"],'blue')==False
```


The test case checks if the function correctly returns `False` when all items in the list are not equal to the given element `'blue'`. The function works correctly in this case. 