```python
def extract_quotation(s):
    return [x for x in s.split('"') if x != ''][1::2]
```
