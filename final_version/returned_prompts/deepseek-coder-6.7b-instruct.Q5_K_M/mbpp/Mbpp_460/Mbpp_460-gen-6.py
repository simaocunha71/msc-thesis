```python
def Extract(lst):
    return [sublist[0] for sublist in lst if isinstance(sublist, list)]

print(Extract([[1, 2], [3, 4, 5], [6,, 7, 8, 9]]))
```

