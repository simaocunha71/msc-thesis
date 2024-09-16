
```python
def count_first_elements(tuple):
    count = 0
    for element in tuple:
        if not isinstance(element, tuple):
            count += 1
    return count
```
