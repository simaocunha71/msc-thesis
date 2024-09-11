"""
Here's a function that checks whether all items in a list are equal to a given element:

```python
def check_element(lst, element):
    return all(i == element for i in lst)
```

You can use the `all()` function to check if all items in the list satisfy the condition in the generator expression. In this case, the condition is `i == element` for each item `i` in the list `lst`. If all items are equal to the given element, the function returns `True`; otherwise, it returns `False`.

To test this function, you can use the `assert` statement. For example, if you call `check_element(["green", "orange", "black", "white"],'blue')`, it will return `False` since not all items in the list are equal to 'blue'. The `assert` statement will then check if the returned value is `False`, and if so, it will raise an error.
"""

# Python code to check whether all items in a list are equal to a given element
def check_element(lst, element):
    return all(i == element for i in lst)

# Test
assert check_element(["green", "orange", "black", "white"],'blue')==False

# This code is contributed by Ankit Rajpurohit (coderbond0).
```
python
```
