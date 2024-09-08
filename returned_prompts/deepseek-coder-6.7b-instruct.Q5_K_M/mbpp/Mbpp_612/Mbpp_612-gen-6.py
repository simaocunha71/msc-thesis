```python
def merge(lst):
    return [list(x) for x in zip(*lst)]

print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']]))
```

This will return:
```
[['x', 'a', 'm'], ['y', 'b', 'n']]
```

Explanation:
The function uses Python's built-in `zip` function to group the elements of each sublist together. The `*` operator is used to unpack the sublists. The `list` function is used to convert the tuples returned by `zip` to lists. These lists are