from collections import Counter

def unique_Element(numList):
    count = Counter(numList)
    if len(count) == 1:
        return True
    else:
        return False


# Testing
print(unique_Element([1,1,1])) # True
print(unique_Element([1,2,3])) # False
print(unique_Element([1,2,3,3])) # False

"""
This problem can be solved by using Counter from collections module. Counter is a dictionary subclass specifically for counting hashable objects, like numbers and strings. In Counter, each unique element will be a key and its count will be the value. We can use len(Counter(numList)) to get the number of unique elements in numList. If the length of Counter is 1, that means only one distinct element is in the list and we return True, otherwise, we return False.
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

