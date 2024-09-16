```python
def frequency_lists(lists):
    flattened = [item for sublist in lists for item in sublist]
    return {item: flattened.count(item) for item in set(flattened)}
```