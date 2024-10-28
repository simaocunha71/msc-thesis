```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```


Explanation:
The function `string_to_md5(text)` takes a string `text` as input and returns its MD5 hash equivalent string. If the input string is empty, it returns `None`.

The function uses the `hashlib` library, which is a Python built-in library, to generate the MD5 hash of the input string. The `encode()` function is used to convert the string into bytes, which is required by the `hashlib` library. The `hexdigest()` function is then used to convert the MD5 hash into a hexadecimal string.

The unit test `>>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'` ensures that the function returns the expected MD5 hash for the input string `'Hello world'`. If the function is implemented correctly, it should pass this test.