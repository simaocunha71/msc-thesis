```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()
```



The problem is asking you to create a function that takes a string as input and returns its MD5 hash equivalent string. If the input string is empty, the function should return None.

The unit test provided checks if the function returns the correct MD5 hash for the string 'Hello world'.

Here's how you can solve this problem using Python and the hashlib library:

```
import hashlib

def string_to_md5(text):
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()
```

In this solution, the function first checks if the input string is empty. If it is, the function returns None. Otherwise, it creates a new MD5 hash object using the hashlib.md5() function and passes the input string as bytes to it using the encode() method. Finally, it returns the hexadecimal representation of the MD5 hash using the hexdigest() method.