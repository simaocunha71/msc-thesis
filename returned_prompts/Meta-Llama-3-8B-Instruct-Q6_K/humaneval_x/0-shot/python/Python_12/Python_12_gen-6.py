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
    return max(strings, key=len)
    # The max function with key=len argument returns the item with the maximum value of the key function (in this case, the length of the string). If multiple items have the maximum value, it returns the first one it encounters. This is exactly what we want. If the list is empty, the max function raises an exception. To avoid this, we first check if the list is empty and return None in this case.  # noqa: E501
    # The max function with key=len argument returns the item with the maximum value of the key function (in this case, the length of the string). If multiple items have the maximum value, it returns the first one it encounters. This is exactly what we want. If the list is empty, the max function raises an exception. To avoid this, we first check if the list is empty and return None in this case.  # noqa: E501
    # The max function with key=len argument returns the item with the maximum value of the key function (in this case, the length of the string). If multiple items have the maximum value, it returns the first one it encounters. This is exactly what we want. If the list is empty, the max function raises an exception. To avoid this, we first check if the list is empty and return None in this case.  # noqa: E501
    # The max function with key=len argument returns the item with the maximum value of the key function (in this case, the length of the string). If multiple items have the maximum value, it returns the first one it encounters. This is exactly what we want. If the list is empty, the max function raises an exception. To avoid this, we first check if the list is empty and return None in this case.  # noqa: E501
    # The max function with key=len argument returns the item with the maximum value of the key function (in this case, the length