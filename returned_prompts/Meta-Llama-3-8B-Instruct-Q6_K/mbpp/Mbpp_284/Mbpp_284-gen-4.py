```
def check_element(lst, element):
    return all(i == element for i in lst)
```
This function uses the built-in `all` function, which returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `i == element for i in lst` checks if each element `i` in the list `lst` is equal to the given `element`. If all elements are equal, the function returns `True`; otherwise, it returns `False`. The unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` verifies that the function returns `False` when the list contains elements that are not equal to the given element.