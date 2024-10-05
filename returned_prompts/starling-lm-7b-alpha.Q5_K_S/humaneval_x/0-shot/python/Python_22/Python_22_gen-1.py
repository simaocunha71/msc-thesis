
def filter_integers(values: List[Any]) -> List[int]:
    return [value for value in values if isinstance(value, int)]


# Testing the function

print(filter_integers(['a', 3.14, 5])) # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # Output: [1, 2, 3]






def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Testing the function

print(filter_integers(['a', 3.14, 5])) # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # Output: [1, 2, 3]








def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


# Testing the function

print(filter_integers(['a', 3.14, 5])) # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []])) # Output: [1, 2, 3]







def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_