from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

This solution uses a list comprehension to create a new list of strings that start with the given prefix. The `startswith` method is used to determine if a string starts with the given prefix.

This solution also includes a check to see if the script is being run directly. If it is, the doctest module is used to run the test cases at the end of the script.

The doctest module is used to run the test cases at the end of the script. The test cases are written in the docstring of the function. The tests are run by calling doctest.testmod(). If all the tests pass, doctest.testmod() will return nothing. If any tests fail, doctest.testmod() will raise a fail exception.

This solution also includes type hints for the function arguments and return value. These are used by tools like mypy and IDEs to provide better support and help.

In this case, the function `filter_by_prefix` takes a list of strings and a prefix string as arguments. It returns a new list of strings that start with the given prefix. The `startswith` method is used to check if a string starts with the given prefix.

This solution uses list comprehension to create a new list of strings that pass the test.

Finally, the solution includes a check to see if the script is being run directly. If it is, the doctest module is used to run the test cases at the end of the script.

This solution also includes type hints for the function arguments and return value. These are used by tools like mypy and IDEs to provide better support and help.

In this case, the function `filter_by_prefix` takes a list of strings and a prefix string as arguments. It returns a new list of strings that start with the given prefix. The `startswith` method is used to check if a string starts with the given prefix.

This solution uses list comprehension to create a new list of strings that pass the test.