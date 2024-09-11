"""
Here's a simple function to check whether all the given tuples have equal length or not. It returns True if all the tuples have the same length, and False if at least one tuple has a different length.

Here's the Python code for the function:

"""

def get_equal(tuples):
    for i in range(len(tuples)-1):
        if len(tuples[i]) != len(tuples[i+1]):
            return False
    return True

# Testing the function.
print(get_equal([(11, 22, 33), (44, 55, 66)]))  # Returns True
print(get_equal([(11, 22), (44, 55, 66)]))  # Returns False

```
  
```

```
"""
In the above Python code, the function `get_equal()` takes a list of tuples as an input. It uses a `for` loop to iterate through the list of tuples, comparing the length of each tuple with the length of the next tuple. If the lengths are not equal, the function immediately returns `False`. If all the tuples have the same length, the function returns `True`.

The function is then tested using two examples. The first example, `get_equal([(11, 22, 33), (44, 55, 66)])`, returns `True` because both tuples have the same length (3). The second example, `get_equal([(11, 22), (44, 55, 66)])`, returns `False` because the first tuple has a length of 2, while the second tuple has a length of 3.

By using this function, you can easily determine whether all the given tuples have equal length or not.

```

```
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
