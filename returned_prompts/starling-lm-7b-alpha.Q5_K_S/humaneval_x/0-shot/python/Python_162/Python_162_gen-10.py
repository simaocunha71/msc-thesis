
Here is a function that will take in a string and return its md5 hash equivalent string:

```python
from hashlib import md5

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    else:
        return md5(text.encode()).hexdigest()
```

In this function, we first check if the `text` string is empty. If it is, we return `None`. Otherwise, we use the `md5` function from the `hashlib` module to calculate the md5 hash of the input string. We then use the `hexdigest()` function to convert the hash into a string representation.

To verify the function, you can use the provided doctest example:

```python
print(string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62')
```

This will output `True` if the function correctly returns the expected md5 hash for the given input, and `False` otherwise.

Note that the md5 hash function is case-sensitive, so the md5 hash for 'hello world' will be different from the md5 hash for 'Hello world'.

```python
print(string_to_md5('hello world') == '15f63b89f16504c2a817d33c42108dcb')
```

This will output `True` if the function correctly returns the expected md5 hash for the given input, and `False` otherwise.

```python
print(string_to_md5('') is None)
```

This will output `True` if the function correctly returns `None` for an empty string input, and `False` otherwise.

```python
print(string_to_md5(None) is None)
```

This will output `True` if the function correctly returns `None` for a `None` input, and `False` otherwise.

```