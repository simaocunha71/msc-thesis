    if not strings:
        return None
    max_length = 0
    max_string = strings[0]
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            max_string = s
    return max_string


def all_longest(strings: List[List[str]]) -> List[str]:
    """ Out of list of list of strings, return the longest string of each sublist. Return an empty
    list in case of no sublist with strings. Return None in case the input list is empty.
    >>> all_longest([])
    []
    >>> all_longest([['a', 'b', 'c']])
    ['a']
    >>> all_longest([['a', 'bb', 'ccc'], ['d', 'ee', 'fff']])
    ['ccc', 'fff']
    """
    if not strings:
        return []
    longest_strings = []
    for sublist in strings:
        longest_strings.append(longest(sublist))
    return longest_strings


# Tests
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(all_longest([]))  # []
print(all_longest([['a', 'bb', 'ccc'], ['d', 'ee', 'fff']]))  # ['ccc', 'fff']























































































































































