```python
def extract_quotation(s):
    return [s[i+1:j] for i, c in enumerate(s) if c == '"' for j, c in enumerate(s) if c == '"' and i < j]
```
