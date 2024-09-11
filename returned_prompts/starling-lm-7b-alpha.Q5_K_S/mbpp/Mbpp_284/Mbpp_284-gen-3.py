"""
Here is a Python function that checks if all items in a list are equal to a given element:

```python
def check_element(lst, element):
    return all(i == element for i in lst)
```

To use this function, pass in the list and the element you want to compare. For example, to check if all items in the list `["green", "orange", "black", "white"]` are equal to `'blue'`, you can use the following code:

```python
print(check_element(["green", "orange", "black", "white"],'blue')) # prints False
```

The `check_element` function will return `True` if all items in the list are equal to the given element, and `False` otherwise.

In the provided example, since not all items in the list are equal to `'blue'`, the function will return `False`.
```

python

```python
def check_element(lst, element):
    return all(i == element for i in lst)
```

Explanation:
The `check_element` function takes in a list (`lst`) and an element (`element`) as parameters. It uses a generator expression with the `all` function to check if all items in the list are equal to the given element. The generator expression `(i == element for i in lst)` returns a sequence of boolean values indicating whether each item in the list is equal to the element. The `all` function then checks if all values in the sequence are `True`. If all values are `True`, the `all` function returns `True`, indicating that all items in the list are equal to the element. Otherwise, it returns `False`.

Example usage:
```python
print(check_element(["green", "orange", "black", "white"],'blue')) # prints False
```

In this example, the function is called with the list `["green", "orange", "black", "white"]` and the element `'blue'`. Since not all items in the list are equal to `'blue'`, the function returns `False`.

Note: The `all` function returns `True` if all values in the iterable are `True`,