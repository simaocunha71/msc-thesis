"""
Here's a Python function that checks whether all items in a list are equal to an element:

```python
def check_element(lst, element):
    if all(i == element for i in lst):
        return True
    else:
        return False
```

You can use this function to check whether all items in a list are equal to a given element. For example, the `assert check_element(["green", "orange", "black", "white"],'blue')` statement will return `False` because the first, second and fourth elements in the list are not equal to 'blue'.

This function works by using Python's built-in `all()` function, which returns `True` if all items in an iterable are true. The `all()` function is used in a generator expression, which checks each item in the list to see if it's equal to the given element. If all items are equal to the element, `all()` will return `True` and the function will return `True`. Otherwise, `all()` will return `False` and the function will return `False`.
"""

def check_element(lst, element):
    if all(i == element for i in lst):
        return True
    else:
        return False

# Testing the function
assert check_element(["green", "orange", "black", "white"],'blue') == False
assert check_element(["green", "orange", "black", "white"],'green') == True

# More testing
print(check_element([1, 2, 3], 3))  # True
print(check_element([1, 2, "three"], "three"))  # True
print(check_element([1, 2, 3, 4], 5))  # False
print(check_element([], 1))  # True
```

This code defines a function `check_element` that takes in a list and an element as parameters. The function uses the `all()` function in a generator expression to check if all items in the list are equal to the element. If all items are equal to the element, the function returns `True`; otherwise, it returns `False`.

The code then includes a