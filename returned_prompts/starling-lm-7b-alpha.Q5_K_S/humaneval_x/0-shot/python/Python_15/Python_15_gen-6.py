
def string_sequence(n: int) -> str:
    """
    Using a for loop, iterate through the range from 0 to n and convert each number to a string using the str() function.
    Append each number string to a list using the append() method.
    Use the join() method to concatenate the list elements with a space as the separator.
    Return the resulting string.
    """
    result = []
    for i in range(n+1):
        result.append(str(i))
    return " ".join(result)

# Unit tests
print(string_sequence(0) == "0")
print(string_sequence(5) == "0 1 2 3 4 5")





def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    result = []
    for i in range(n+1):
        result.append(str(i))
    return " ".join(result)

# Unit tests
print(string_sequence(0) == "0")
print(string_sequence(5) == "0 1 2 3 4 5")










































def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    result = []
    for i in range(n+1):
        result.append(str(i))
    return " ".join(result)

# Unit tests
print(string_sequence(0) == "0")
print(string_sequence(5) == "0 