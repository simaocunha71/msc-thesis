
```python
import hashlib

def string_to_md5(text):
    if text == "":
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

This function uses the hashlib library in python to create an md5 hash of the input string. The input string is encoded before being hashed to ensure it is in the correct format.

```python
print(string_to_md5('Hello world'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62
```

In the test case, the string 'Hello world' is passed in to the function. The function returns the md5 hash of 'Hello world', which is '3e25960a79dbc69b674cd4ec67a72c62'.
"""


def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '2ef7bde608ce5404e97d5f042f95f89f1c232871'
    """

    if text == "":
        return None
    return hashlib.sha1(text.encode()).hexdigest()


def string_to_sha256(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha256('Hello world') == '7b5c52d3bb95600e09c85081c959c0d141d9f5d9b9c3d9cab9b5e9c0f5f9a7a1e'
    """

    if text == "":
        return None
    return hashlib.sha256(text.encode()).hexdigest()
```

This function uses the