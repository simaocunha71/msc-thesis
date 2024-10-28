    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print(filter_by_substring([] , 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    result = [s for s in strings if substring in s]
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print(filter_by_substring([] , 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print(filter_by_substring([] , 'a'))  # []
    print(filter_by_substring(['abc', 'b