    if not strings:
        return None
    longest_str = strings[0]
    for s in strings[1:]:
        if len(longest_str) < len(s):
            longest_str = s
    return longest_str


# Testing
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'


def longest_v2(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)


# Testing
print(longest_v2([]))  # None
print(longest_v2(['a', 'b', 'c']))  # 'a'
print(longest_v2(['a', 'bb', 'ccc']))  # 'ccc'


def longest_v3(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    return sorted(strings, key=len, reverse=True)[0]


# Testing
print(longest_v3([]))  # None
print(longest_v3(['a', 'b', 'c']))  # 'a'
print(longest_v3(['a', 'bb', 'ccc']))  # 'ccc'


def longest_v4(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len, default=None)


# Testing
