```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```


This function takes a string input, checks if it's empty, and if so, returns None. If the string is not empty, it uses the hashlib library to generate the MD5 hash of the string, and returns the hexadecimal representation of that hash.

Note: The hashlib library is a built-in Python library, so you don't need to install anything extra to use it.

The test case provided checks if the function returns the correct MD5 hash for the input string 'Hello world'. The expected output is '3e25960a79dbc69b674cd4ec67a72c62', which is the MD5 hash of the input string. The function should return this exact string if the test case is correct.