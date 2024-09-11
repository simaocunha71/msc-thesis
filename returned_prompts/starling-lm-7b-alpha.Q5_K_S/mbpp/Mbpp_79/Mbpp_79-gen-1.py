Here is a Python function that checks whether the length of the word is odd or not:

```python
def word_len(word):
    """
    This function checks whether the length of the word is odd or not.
    """
    return len(word) % 2 != 0
```

In this function, we use the modulus operator `%` to check if the length of the word is divisible by 2. If the length is divisible by 2, the result of `len(word) % 2` will be 0, which means the length of the word is even. If the length is not divisible by 2, the result of `len(word) % 2` will be 1, which means the length of the word is odd. 

The function returns `True` if the length of the word is odd, and `False` if the length of the word is even. 

To test the function, you can use the `assert` statement like this:

```python
assert word_len("Hadoop") == False
```

This assertion will pass if the length of the word "Hadoop" is odd, and fail if the length of the word "Hadoop" is even.

```python
def word_len(word):
    """
    This function checks whether the length of the word is odd or not.
    """
    return len(word) % 2 != 0
```

This Python function will return `True` if the length of the word is odd, and `False` if the length of the word is even.

To test the function, you can use the `assert` statement like this:

```python
assert word_len("Hadoop") == False
```

This assertion will pass if the length of the word "Hadoop" is odd, and fail if the length of the word "Hadoop" is even.

```python
def word_len(word):
    """
    This function checks whether the length of the word is odd or not.
    """
    return len(word) % 2 != 0
```

This Python function will return `True` if the length of the word is odd, and `False