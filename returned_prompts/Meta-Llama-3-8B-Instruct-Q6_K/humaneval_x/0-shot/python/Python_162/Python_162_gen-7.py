```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()
```



In this solution, we use the `hashlib` library to create an MD5 hash object. We then update the hash object with the input text, encoding it as UTF-8 bytes. Finally, we return the hexadecimal representation of the hash object using the `hexdigest()` method.

We also added a check at the beginning of the function to return `None` if the input text is an empty string. This is in line with the problem statement, which specifies that the function should return `None` for an empty input string.