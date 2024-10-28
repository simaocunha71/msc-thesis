
```python
import hashlib

def string_to_md5(text):
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()
```

This function uses the built-in hashlib module to create an md5 hash of the input string. The hexdigest() method is used to convert the md5 hash to a string of hexadecimal characters. If the input string is empty, the function returns None.

Note: The hexadecimal string returned by the hexdigest() method includes both the hash type identifier ("MD5") and the hash value itself. However, in the question, only the hash value is required, so it may be necessary to modify the function to return only the hash value.

This function is case-sensitive. If you want it to be case-insensitive, you can add a line to convert the input string to lowercase or uppercase before hashing it.

Also, note that md5 is considered to be weak and not suitable for cryptographic use. If you need to hash passwords or other sensitive data, it's better to use a strong hash function like bcrypt or scrypt.
