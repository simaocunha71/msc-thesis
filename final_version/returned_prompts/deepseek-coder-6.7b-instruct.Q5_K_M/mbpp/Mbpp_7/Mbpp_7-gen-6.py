```python
def find_char_long(s, char_long=4):
    return [word for word in s.split() if len(word) >= char_long]

print(set(find_char_long('Please move back to stream')))
```

