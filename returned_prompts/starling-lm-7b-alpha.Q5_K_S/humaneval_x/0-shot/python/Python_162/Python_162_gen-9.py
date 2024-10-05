
To solve this problem, we can follow these steps:

1. Import the `hashlib` module, which provides the functionality to compute the MD5 hash of a string.
2. Define the `string_to_md5` function that takes a `text` parameter.
3. Inside the function, check if the `text` is an empty string. If it is, return `None`.
4. If the `text` is not an empty string, use the `hashlib.md5()` function to compute the MD5 hash of the `text`. Convert the hash to a hexadecimal string using the `hexdigest()` method.
5. Return the MD5 hash string.

Here's the modified code that implements the above steps:

```python
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```

Now, you can use the `string_to_md5` function to get the MD5 hash of any string. For example, `string_to_md5('Hello world')` will return `'3e25960a79dbc69b674cd4ec67a72c62'`.

Note: Make sure to import the `hashlib` module before using it in your code.

```python
import hashlib
```

```python
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
       