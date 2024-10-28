    result = []
    for word in words:
        if word not in result:
            result.append(word)

    return result


def find_longest(strings: List[str]) -> str:
    """ Find the longest string in the list of strings """
    longest = strings[0]
    for string in strings:
        if len(longest) < len(string):
            longest = string

    return longest


def is_subsequence(string1: str, string2: str) -> bool:
    """ Check if string1 is a subsequence of string2.
    A subsequence is a string that can be derived from another string by deleting some or no characters
    without changing the order of the remaining characters.
    >>> is_subsequence('', '')
    True
    >>> is_subsequence('', 'cat')
    True
    >>> is_subsequence('cat', '')
