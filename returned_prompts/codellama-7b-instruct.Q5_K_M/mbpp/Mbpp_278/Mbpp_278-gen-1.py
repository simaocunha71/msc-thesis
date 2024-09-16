```python
def count_first_elements(tup):
    count = 0
    for element in tup:
        if not isinstance(element, tuple):
            count += 1
    return count
```
