"""
def test_duplicate(array):
    set_array = set(array)
    if len(set_array) != len(array):
        return True
    else:
        return False
"""

# Here's a Python solution to the problem above:

def has_duplicates(nums):
    """
    Args:
        nums(list): a list of integers

    Returns:
        bool: True if there is any duplicate in the list, False otherwise
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Here's a Python solution to the problem above:

def test_duplicate(array):
    set_array = set(array)
    if len(set_array) != len(array):
        return True
    else:
        return False


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
