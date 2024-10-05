    return [s for s in strings if substring in s]


def filter_by_substring_v2(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_v2([], 'a')
    []
    >>> filter_by_substring_v2(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    return [s for s in strings if substring in s]


def filter_by_substring_v3(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_v3([], 'a')
    []
    >>> filter_by_substring_v3(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result


def filter_by_substring_v4(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_v4([], 'a')
    []
    >>> filter_by_substring_v4(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result


def filter_by_substring_v5(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring_v5([], 'a')
    []
    >>> filter_by_substring_v5(['abc', 'bacd', 'cde