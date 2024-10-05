from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

This solution uses a list comprehension to iterate over the input list of strings and select only those that start with the specified prefix. The function `startswith()` is a built-in Python method that checks if a string starts with a given prefix. The function returns the filtered list of strings.

The `if __name__ == "__main__":` statement is used to run the doctest module when the script is run directly. This will check the function's documentation string for any examples and run them, reporting any failures.

The `doctest.testmod()` function returns a test summary, which includes the total number of tests, the number of successful tests, and the number of failed tests. If all tests are successful, it returns `(0, 0, 0, 0)`.

Note: The doctest module does not check the order of elements in the lists. If you need to check the order, you would need to write a more complex function.
"""

# 11. Write a Python program that reads a file and counts the frequency of words in the file.

"""
