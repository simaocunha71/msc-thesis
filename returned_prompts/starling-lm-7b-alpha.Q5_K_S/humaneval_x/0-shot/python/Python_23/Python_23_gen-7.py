
Here is a function that returns the length of a given string:

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

The `len()` function in Python returns the number of characters in the given string. So, by using `len(string)`, we can find the length of the given string and return it.

You can use this function by calling it with a string as an argument. For example, `strlen('')` will return 0 (because an empty string has no characters), and `strlen('abc')` will return 3 (because the string 'abc' has 3 characters).

To test the function, you can use a doctest. A doctest is a way of testing a function by including example usage in the function's docstring. In this case, we can include the example usage `strlen('')` and `strlen('abc')` in the docstring and use the `>>>` symbol to separate the function call from the expected output.

The doctest will then automatically check if the function's output matches the expected output for the given examples.

Note that the `len()` function is a built-in Python function, so you don't need to define it yourself.

I hope this helps! Let me know if you have any more questions.

Here are some additional resources for learning more about Python strings and doctests:

- [Python Strings](https://docs.python.org/3/library/stdtypes.html#text)
- [Python Doctests](https://docs.python.org/3/library/doctest.html)

If you found this answer helpful, please let me know!

```

```