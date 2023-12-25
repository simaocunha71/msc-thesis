from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    else:
        max_len = min(str.length for str in strings)
        for (i, str_) in enumerate(strings):
            if (max_len - len(str_)) > (max_len - len(max(strings, key=lambda s: len(s)))):
                return str_.strip()
    else:
        return None


if __name__ == '__main__':
    print(longest([1, 2, 3, 4, 5]))