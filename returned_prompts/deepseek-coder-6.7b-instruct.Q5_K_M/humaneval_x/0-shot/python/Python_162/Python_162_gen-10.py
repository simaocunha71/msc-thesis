
```python
import hashlib

def string_to_md5(text):
    if text:
        return hashlib.md5(text.encode()).hexdigest()
```

In this function, we use the hashlib library to generate the md5 hash of the input string. The encode() method is used to convert the string into bytes before the md5 hash is generated.
"""


