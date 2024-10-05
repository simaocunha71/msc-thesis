```python
import hashlib

def string_to_md5(text):
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()
```

This function first checks if the input string is empty. If it is, it returns None. Otherwise, it encodes the string using the 'encode()' method and then uses the 'md5()' function from the hashlib module to generate the MD5 hash. The resulting hash is then converted to a hexadecimal string using the 'hexdigest()' method.