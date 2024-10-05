
Here is a Python function that returns the length of a given string:

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

You can use the `len()` function in Python to get the length of a string. The function `strlen()` takes a string as input and returns its length as an integer. 

For example, if you call `strlen('')`, it will return 0, because an empty string has no characters. If you call `strlen('abc')`, it will return 3, because the string 'abc' has three characters. 

To use this function, you can simply call it and pass the string you want to measure as an argument. For example, `strlen('hello')` will return 5, because the string 'hello' has five characters. 

This function can be useful in various situations where you need to know the length of a string, such as when you want to iterate over all the characters in a string, or when you want to check if a string is shorter or longer than a certain length.

I hope this helps! Let me know if you have any more questions.

```python
# Testing the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('hello'))  # Output: 5
```

```python
# Another way of testing the function using doctest module
from doctest import *

def test_strlen():
    """ Test the strlen function """
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('hello') == 5

if __name__ == '__main__':
    test_strlen()
```

```python
# Testing the function using unittest module
import unittest

class TestStrlen(unittest.TestCase):
    """ Test the strlen function """

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_abc(self):
        self.assertEqual(strlen('abc'), 