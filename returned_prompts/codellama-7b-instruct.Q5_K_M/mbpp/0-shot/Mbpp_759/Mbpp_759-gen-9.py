```python
def is_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
```

