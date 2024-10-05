from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
    # The function takes a list of strings and a prefix as input.
    # It uses a list comprehension to create a new list that includes only the strings
    # that start with the given prefix. The startswith method is used to check if a string
    # starts with a certain prefix. The result is a new list of strings that start with the given prefix.
    # The function returns this new list.
    # The function is tested with the provided unit tests. The first test is an empty list
    # and the second test is a list with strings that start with the given prefix. The function
    # correctly returns the expected result in both cases.