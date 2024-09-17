```
def check_element(lst, element):
    return all(i == element for i in lst)
```
The problem is asking you to create a function that takes a list and an element as input, and returns True if all items in the list are equal to the given element, and False otherwise.

The unit test `assert check_element(["green", "orange", "black", "white"],'blue')==False` suggests that the function should return False if the list contains any item that is not equal to the given element.

Here's a Python solution that uses the built-in `all` function and a generator expression:

```
def check_element(lst, element):
    return all(i == element for i in lst)
```

This function works by iterating over each item in the list and checking if it's equal to the given element. The `all` function returns True if all items in the iterable (in this case, the generator expression) are true. If any item is not equal to the element, the `all` function will return False. If all items are equal to the element, the `all` function will return True.