```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```


Test:
```
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
assert string_to_md5('') is None
```


The function `string_to_md5` takes a string as an input and returns its md5 hash equivalent string. If the input string is empty, it returns `None`. The function uses the hashlib library in Python, which provides a common interface to many different secure hash and message digest algorithms.

The `hashlib.md5()` function is used to create an md5 hash object, and the `hexdigest()` function is used to get the md5 hash as a hexadecimal string.

The test cases ensure that the function works correctly for a non-empty string and an empty string. For a non-empty string, the function should return the correct md5 hash. For an empty string, the function should return `None`.