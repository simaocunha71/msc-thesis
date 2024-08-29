```python
def min_k(lst, k):
    lst.sort(key = lambda x: x[1])
    return lst[:k]

print(min_k([('Manjeet', 10),  ('Akshat', 4),  ('Akash', 2),  ('Nikhil', 8)], 2))
```

