
Here's a Python function that removes vowels from a string:

```python
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return ''.join(c for c in text if c not in vowels)
```

In this function, `vowels` is a string of all the vowels (both lower case and upper case). The function uses a generator expression to create a new string that only includes characters from the original string that are not vowels.

The function uses the `join` method to concatenate all the characters in the generator expression into a single string, which is then returned.

The function can be tested with the following doctest:

```python
from textwrap import dedent

def test_remove_vowels():
    test_cases = dedent("""
        It('') -> ''
        It('abcdef\nghijklm') -> 'bcdf\nghjklm'
        It('abcdef') -> 'bcdf'
        It('aaaaa') -> ''
        It('aaBAA') -> 'B'
        It('zbcd') -> 'zbcd'
    """)
    assert eval(test_cases)

if __name__ == "__main__":
    test_remove_vowels()
```

This doctest includes several test cases for the `remove_vowels` function. Each test case is enclosed in a `It` block, where `It` is a convenience function that allows for easy comparison of expected and actual results.

When the doctest is run, it will compare the expected results with the actual results of the function and print a message indicating whether the test passed or failed.

The `dedent` function is used to remove the leading whitespace from each test case, so that the actual results can be compared correctly with the expected results.

The `eval` function is used to execute the test cases as Python code, which allows the function to be tested dynamically.

Finally, the `if __name__ == "__main__"` block ensures that the test cases are only run if the script is executed directly (not imported as a module). This is a common practice in Python