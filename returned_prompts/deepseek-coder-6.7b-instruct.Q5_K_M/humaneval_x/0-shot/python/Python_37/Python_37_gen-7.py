
```python
def sort_even(l: list):
    even_list = sorted([l[i] for i in range(0, len(l), 2)])
    new_l = [even_list.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
    return new_l
```

