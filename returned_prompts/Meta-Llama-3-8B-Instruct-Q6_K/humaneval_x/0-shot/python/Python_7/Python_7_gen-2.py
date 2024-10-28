from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    return [s for s in strings if substring in s]
    # This is a list comprehension that iterates over each string in the input list
    # and checks if the substring is present in the string. If it is, the string is
    # included in the output list. If not, it is not included. The resulting list
    # is returned.