
Here is a Python program that defines a function `strlen` that accepts a string as an argument and returns the length of the string:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

You can use the `len()` function in Python to get the length of a string. The `len()` function takes a sequence as an argument and returns the number of items in the sequence. In this case, the sequence is a string and the length is the number of characters in the string.

To test the function, you can use the `doctest` module in Python, which allows you to include test cases in the function's docstring. The `>>>` symbol is used to indicate the input and the `...` symbol is used to indicate the expected output.

In the example provided, the `strlen` function is tested with two different strings: an empty string and a string with three characters. The expected output for the empty string is 0, and for the string with three characters is 3.

To run the tests, you can use the `doctest.testmod()` function in Python, which will execute the `doctest` statements in the function's docstring and check if the expected output matches the actual output. If all tests pass, the function is correctly implemented.

```python
import doctest

doctest.testmod(locale='en_US')
```

The `locale` parameter is used to specify the language and region settings for the tests. In this case, the locale is set to 'en_US' to match the English language and United States region.

By running the `doctest.testmod()` function, you can verify that the `strlen` function is correctly implemented and returns the length of a given string.

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

```python
import doctest

doctest.testmod(locale='en_US')