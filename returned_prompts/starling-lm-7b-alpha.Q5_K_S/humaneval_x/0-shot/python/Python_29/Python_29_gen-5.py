    return [string for string in strings if string.startswith(prefix)]


if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))




def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
    ...



def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
    ...




def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [