```
def check_element(lst, element):
    return all(item == element for item in lst)
```





The task is to create a function that takes a list and an element as input, and checks if all items in the list are equal to the given element.

The provided unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` helps clarify the expected behavior of the function. It indicates that the function should return `True` if all items in the list are equal to the given element, and `False` otherwise.

The solution to this problem is a simple `all` function combined with a generator expression. The `all` function returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `item == element for item in lst` checks if each item in the list is equal to the given element. If any item is not equal, the `all` function will return `False`.

Here's the implementation:
```
def check_element(lst, element):
    return all(item == element for item in lst)
```
This function will return `True` if all items in the list are equal to the given element, and `False` otherwise.