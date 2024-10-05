from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
# This function uses the built-in join() function in Python, which concatenates all items in an iterable (like a list or tuple) into a single string. The items must be strings. In this case, we pass our list of strings to the join() function, which returns the concatenated string. If the list is empty, an empty string is returned, as shown in the unit tests.