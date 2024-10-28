```python
def text_lowercase_underscore(input_string):
    import re
    pattern = r"[a-z]+(_[a-z]+)+"
    return bool(re.search(pattern, input_string))
```
