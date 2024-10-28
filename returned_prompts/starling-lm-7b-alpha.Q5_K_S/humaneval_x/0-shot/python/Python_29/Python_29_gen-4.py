    return [s for s in strings if s.startswith(prefix)]


def filter_by_length(strings: List[str], min_length: int, max_length: int = None) -> List[str]:
    """ Filter an input list of strings only for ones that are within a given range of lengths.
    >>> filter_by_length([], 2, 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 3)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2)
    ['abc', 'bcd']
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 5)
    ['abc', 'bcd', 'cde']
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 1, 5)
    ['abc', 'bcd', 'cde', 'array']
    """

    if max_length is None:
        return [s for s in strings if len(s) >= min_length]
    else:
        return [s for s in strings if len(s) >= min_length and len(s) <= max_length]


def filter_by_length_and_prefix(strings: List[str], min_length: int, max_length: int = None, prefix: str = '') -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix and are within a given range of lengths.
    >>> filter_by_length_and_prefix([], 2, 3, 'a')
    []
    >>> filter_by_length_and_prefix(['abc', 'bcd', 'cde', 'array'], 2, 3, 'a')
    []
    >>> filter_by_length_and_prefix(['abc', 'bcd', 'cde', 'array'], 2, 5, 'a')
    ['abc']
    >>> filter_by_length_and_prefix(['abc', 'bcd', 'cde', 'array'], 1, 5