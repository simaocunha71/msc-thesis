```python
def remove_nested(tup):
    new_tup = []
    for i in tup:
        if not isinstance(i, tuple):
            new_tup.append(i)
    return tuple(new_tup)

print(remove_nested((1, 5, 7, (4, 6), 10)))
```

