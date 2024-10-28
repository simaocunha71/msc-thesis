```python
def is_decimal(s):
    return s.count('.') == 1 and s.replace('.', '').isdigit() and len(s.split('.')[1]) <= 2
```

