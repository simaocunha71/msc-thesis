"""
To check whether a tuple has any none value or not, you can follow the below steps:

1. Iterate through the tuple using the for loop.
2. For each iteration, check if the tuple element is none or not. If the element is none, return True.
3. If no none value is found, return False.

Here's the Python function that implements the above steps:
"""

def check_none(tup):
    """
    Check if the given tuple has any none value or not.

    Parameters:
    tup (tuple): The given tuple.

    Returns:
    bool: True if the tuple has any none value, False otherwise.
    """
    for elem in tup:
        if elem is None:
            return True
    return False

# Test the function
print(check_none((10, 4, 5, 6, None)))  # Output: True
print(check_none((10, 4, 5, 6)))  # Output: False


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

``