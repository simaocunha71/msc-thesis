
```python
def combinations_colors(lst, n):
    return [x for x in itertools.product(lst, repeat=n)]

print(combinations_colors(["Red","Green","Blue"],1))
```

