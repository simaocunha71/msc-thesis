```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```


Note:

*   The `hashlib` library is used to create the MD5 hash.
*   The `text.encode()` is used to convert the string to bytes, because `hashlib` requires bytes-like object.
*   The `hexdigest()` function is used to get the hexadecimal representation of the hash value. 
*   If the input string is empty, the function returns `None`. 

The unit test provided checks if the function correctly calculates the MD5 hash for the string 'Hello world'. The expected output is '3e25960a79dbc69b674cd4ec67a72c62'. The function should return this value when given the input 'Hello world'. 