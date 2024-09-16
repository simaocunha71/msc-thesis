```python
def remove_length(string, k):
    words = string.split()
    return ' '.join([word for word in words if len(word) != k])
```
