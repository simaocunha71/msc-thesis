    return ''.join(strings)


# Test cases
assert concatenate([]) == ''
assert concatenate(['a', 'b', 'c']) == 'abc'
assert concatenate(['', 'a', 'b', 'c']) == 'abc'
assert concatenate(['a', 'b', 'c', '']) == 'abc'



def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['', 'a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', ''])
    'abc'
    """
    return ''.join(strings)


# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['', 'a', 'b', 'c']))  # 'abc'
print(concatenate(['a', 'b', 'c', '']))  # 'abc'



def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['', 'a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', ''])
    'abc'
    """
    return ''.join(strings)


# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['', 'a', 'b', 'c']))  # 'abc'
print(concatenate(['a', 'b', 'c', '']))  # 'abc'



def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single