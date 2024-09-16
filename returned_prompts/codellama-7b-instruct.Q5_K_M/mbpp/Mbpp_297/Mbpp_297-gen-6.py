```python
def flatten_list(nested_list):
    res = []
    for element in nested_list:
        if isinstance(element, list):
            res.extend(flatten_list(element))
        else:
            res.append(element)
    return res
```
