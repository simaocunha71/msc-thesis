

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    for _ in string:
        count += 1
    return count


print(strlen('abc'))

# OR

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

print(strlen('abc'))

# OR

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return sum(1 for _ in string)

print(strlen('abc'))


# OR

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return sum([1 for _ in string])

print(strlen('abc'))
```

In all these functions, we traverse through the string and count each character to find its length. The time complexity of this function is O(n), where n is the length of the string.


### 2. Sum of elements in a list

