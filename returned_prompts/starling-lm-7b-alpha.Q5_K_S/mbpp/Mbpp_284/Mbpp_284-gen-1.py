```
def check_element(list, element):
    for i in list:
        if i != element:
            return False
    return True
```

Also, Here is a one-liner for the same:
```
def check_element(list, element):
    return True if all(x == element for x in list) else False
```

Explanation:
The function `check_element` is defined to take a list and an element as input. It uses a for loop to iterate through each item in the list. If any item in the list is not equal to the given element, the function returns False, indicating that not all items in the list are equal to the given element. If all items in the list are equal to the given element, the function returns True, indicating that all items in the list are equal to the given element.

The one-liner version of the function uses the built-in `all()` function along with a generator expression to achieve the same result. The `all()` function returns True if all elements in the generator expression evaluate to True, otherwise it returns False. In this case, the generator expression `(x == element for x in list)` checks if each item in the list is equal to the given element. If all items are equal to the given element, the `all()` function returns True and the one-liner function returns True. Otherwise, the `all()` function returns False and the one-liner function returns False.

Both versions of the function can be used to check whether all items in a list are equal to a given element.

The `assert` statement is used to check if the function `check_element` returns the expected result when given a specific list and element. In this case, the `assert` statement checks if `check_element(["green", "orange", "black", "white"],'blue')` is False. If the function returns True instead of False, the `assert` statement will raise an `AssertionError` with the message "Assertion 'False' failed".
```

```

```

```python

```

```

```

```

```

```

```

```

```python

```