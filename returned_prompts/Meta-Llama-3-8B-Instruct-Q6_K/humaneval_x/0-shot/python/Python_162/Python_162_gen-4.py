```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()
```


This code defines a function `string_to_md5` that takes a string `text` as input and returns its MD5 hash equivalent string. If the input string is empty, it returns `None`. The function uses the `hashlib` library to generate the MD5 hash.

The unit test provided ensures that the function returns the correct MD5 hash for the input string `'Hello world'`. The expected output is `'3e25960a79dbc69b674cd4ec67a72c62'`. This test can be used to verify the correctness of the function.