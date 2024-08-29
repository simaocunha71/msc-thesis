```python
def pack_consecutive_duplicates(lst):
    packed = []
    i = 0
    while i < len(lst):
        start = i
        while i < len(lst) - 1 and lst[i] == lst[i+1]:
            i += 1
        packed.append(lst[start:i+1])
        i += 1
    return packed
```

