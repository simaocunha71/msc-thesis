```python
def find_tuples(lst, k):
    return [tup for tup in lst if all(el % k == 0 for el in tup)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
```

