
To solve this problem, we can use Python's built-in `hashlib` library, which provides a `md5()` function that can be used to generate the MD5 hash of a string.

Here's a step-by-step guide on how to use the `md5()` function to solve this problem:

1. First, import the `hashlib` library in your Python program:
```python
import hashlib
```

2. Next, define the `string_to_md5()` function. This function takes a string `text` as an input, and returns the MD5 hash equivalent string of that text.

3. Inside the `string_to_md5()` function, check if the `text` string is empty. If it is, return `None`.

4. If the `text` string is not empty, use the `md5()` function from the `hashlib` library to generate the MD5 hash of the `text` string. Store the result in a variable called `md5_hash`.

5. Finally, return the `md5_hash` variable, which will contain the MD5 hash equivalent string of the input `text` string.

Here's the complete implementation of the `string_to_md5()` function:
```python
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash
```

You can test the `string_to_md5()` function with the provided test case in the question:
```python
print(string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62')  # Should print: True
```

This will return `True`, indicating that the `string_to_md5()` function correctly generates the MD5 hash equivalent string for the input `'Hello world'`.

I hope this helps