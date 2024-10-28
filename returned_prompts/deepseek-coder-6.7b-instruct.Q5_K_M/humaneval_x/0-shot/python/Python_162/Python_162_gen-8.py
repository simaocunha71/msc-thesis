
```python
import hashlib

def string_to_md5(text):
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()
```


### 2. Write a Python function that takes a string and returns the frequency of each character in the string.

