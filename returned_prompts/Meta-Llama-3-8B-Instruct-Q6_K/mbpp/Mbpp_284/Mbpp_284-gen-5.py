```
def check_element(lst, element):
    return all(i == element for i in lst)
```


The function `check_element` takes a list `lst` and an element `element` as input. It returns `True` if all items in the list are equal to the given element, and `False` otherwise.

The unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` ensures that the function returns `False` when the list contains elements that are not equal to the given element. This test case helps to clarify the expected behavior of the function.

In this solution, the `all` function is used with a generator expression to check if all items in the list are equal to the given element. The generator expression `i == element for i in lst` iterates over the list and checks if each item is equal to the element. If any item is not equal, the `all` function returns `False`. If all items are equal, the `all` function returns `True`.