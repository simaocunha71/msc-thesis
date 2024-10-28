
```python
import hashlib

def string_to_md5(text):
    if text == "":
        return None
    else:
        hash_object = hashlib.md5(text.encode())
        return hash_object.hexdigest()
```

This function works by importing the hashlib module, which provides the functionality needed to compute MD5 hashes. If the input string is empty, the function returns None. Otherwise, it creates an MD5 hash object and uses it to compute the hexadecimal representation of the MD5 hash of the input string. The hashlib.md5() function is used to create the hash object, and the .encode() method is used to convert the input string into bytes. The .hexdigest() method is then used to get the hexadecimal representation of the hash.

Note: The hashlib module is a part of the standard library in Python, so it doesn't need to be installed separately.
