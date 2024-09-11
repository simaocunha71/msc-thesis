def all_unique(lst):
    """
    Check if all elements of a given list are unique
    """
    if len(lst) == len(set(lst)):
        return True
    else:
        return False

# Test
assert all_unique([1,2,3]) == True

# More tests
assert all_unique([1,1,2,3]) == False
assert all_unique([1,2,2,3]) == False
assert all_unique([1,2,3,4,4,5,6]) == False
assert all_unique([1,2,3,4,5,6]) == True



# Explanation
# The function all_unique(lst) checks if the length of the list is equal to the length of the set of the list.
# If the length of the list is equal to the length of the set of the list, it means all elements in the list are unique, and the function returns True.
# Otherwise, it means there are duplicate elements in the list, and the function returns False.

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