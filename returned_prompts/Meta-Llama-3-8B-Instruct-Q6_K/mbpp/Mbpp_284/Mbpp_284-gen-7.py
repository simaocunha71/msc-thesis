```
def check_element(lst, element):
    return all(i == element for i in lst)
```





The function `check_element` takes in a list `lst` and an element `element`. It returns `True` if all items in the list are equal to the given element, and `False` otherwise.

The unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` helps to clarify the expected behavior of the function. It indicates that the function should return `False` when the list contains elements other than the given element.

The implementation uses the `all` function and a generator expression to check if all items in the list are equal to the given element. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `i == element for i in lst` checks if each item `i` in the list is equal to the given element. If any item is not equal to the element, the `all` function will return `False`. If all items are equal to the element, the `all` function will return `True`.