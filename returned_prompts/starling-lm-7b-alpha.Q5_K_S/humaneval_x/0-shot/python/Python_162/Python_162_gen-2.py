
To solve this problem, we can use the hashlib library in Python to calculate the MD5 hash of the input string. Here's a step-by-step breakdown of the solution:

1. Import the hashlib library, which provides the md5() function for calculating MD5 hashes.
2. Define the string_to_md5() function that takes a 'text' parameter of type str.
3. Check if the 'text' parameter is an empty string. If it is, return None, as specified in the problem statement.
4. Use the hashlib.md5() function to calculate the MD5 hash of the 'text' string. This function takes the 'text' string as an argument and returns a hash object.
5. Use the hexdigest() method of the hash object to obtain the hash value as a string. This method converts the hash value from binary format to a hexadecimal string.
6. Return the MD5 hash string.

Here's the Python code for the solution:

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
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()
```

You can test the function with the provided example in the problem statement:

```python
print(string_to_md5('Hello world'))  # Output: '3e25960a79dbc69b674cd4ec67a72c62'
```

This will return the MD5 hash equivalent string for the input 'Hello world', as specified in the problem statement.

Note: The string_to_md5() function is case-sensitive, meaning that the MD5 hash will be different for different cases of the same text. For example, 'Hello world' will have a different MD5 hash compared to '