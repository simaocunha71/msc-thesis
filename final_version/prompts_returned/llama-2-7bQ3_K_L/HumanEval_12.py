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
    if len(strings) == 0:
        return None
    max_length = max((len(s.lower()) for s in strings))
    if max_length >= len(strings[0]):
        # check all strings that are of the same length as max_length
        for i, s in enumerate(strings):
            if len(s.lower()) == max_length:
                return s[i:]
    elif len(strings[0]) >= max_length:
        # check all strings that are not equal to any of the ones that were already checked
        for i, s in enumerate(strings):
            if len(s.lower()) == max_length and i != 0:
                return s
    else:
        return min(strings)[1:]
