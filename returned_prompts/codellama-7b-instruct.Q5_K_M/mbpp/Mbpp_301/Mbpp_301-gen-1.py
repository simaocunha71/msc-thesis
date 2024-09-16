```python
def dict_depth(d):
    return max(map(dict_depth, d.values())) if isinstance(d, dict) else 1
```
