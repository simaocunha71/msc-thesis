"""
Here is a possible solution:

```python
def check_element(input_list, element):
    """
    Takes a list and an element and checks whether all items in the list are equal to the given element.
    >>> check_element(["green", "orange", "black", "white"],'blue')
    False
    """
    return all(x == element for x in input_list)
```

This function iterates through the list using a generator expression. It compares each element in the list to the given element and returns True if all elements in the list are equal to the given element and False otherwise.
"""

# Python 3 program to find if all items in a
# list are equal to the given element

def check_element(input_list, element):
    # Returns True if all items in the list
    # are equal to the given element
    return all(x == element for x in input_list)

# Driver code

# check if all items in list are equal to 'blue'
print(check_element(["green", "orange", "black", "white"],'blue'))
```

Here is a test:

```python
print(check_element(["green", "orange", "black", "white"],'blue'))  # False
print(check_element(["green", "green", "green", "green"],'green'))  # True
```

This will output:

```
False
True
```

"""

# Python 3 program to find if all items in a
# list are equal to the given element

def check_element(input_list, element):
    # Returns True if all items in the list
    # are equal to the given element
    return all(x == element for x in input_list)

# Driver code

# check if all items in list are equal to 'blue'
print(check_element(["green", "orange", "black", "white"],'blue'))  # False
print(check_element(["green", "green", "green", "green"],'green'))  # True
```

This will output:

```
False
True
```
