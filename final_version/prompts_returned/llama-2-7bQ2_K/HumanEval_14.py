from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if not string:
        return []

    res = [prefix for prefix in string.split()] + [string]

    return list(set(res))  # Remove duplicates
