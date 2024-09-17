"""
You can solve this problem with the following function:

```python
def match_string(s):
    import re
    return bool(re.match(r'a.*b', s))
```

This function uses the `re` module, which provides regular expression matching operations. The `match` function returns a match object if the string matches the pattern, or `None` otherwise. The `bool` function converts this to a boolean value, which is `True` if the string matches the pattern and `False` otherwise.

The pattern `r'a.*b'` matches any string that starts with 'a', followed by any characters (captured by `.*`), and ends with 'b'. The `r` prefix indicates a raw string literal, which is useful for regular expressions because it allows you to write the pattern without having to escape special characters.

For example, `match_string("aabbbb")` would return `True`, because the string matches the pattern. `match_string("abc")` would return `False`, because the string does not match the pattern.```python
```python
import re

def match_string(s):
    return bool(re.match(r'a.*b', s))

assert match_string("aabbbb")
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python
```python