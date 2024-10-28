```python
def drop_empty(dct):
    return {k: v for k, v in dct.items() if v is not None}
```
