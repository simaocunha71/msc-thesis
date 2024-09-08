```python
def count_first_elements(tup):
    cnt = 0
    for i in tup:
        if isinstance(i, tuple):
            break
        cnt += 1
    return cnt

print(count_first_elements((1, 5, 7, (4, 6), 10)))  # 3
```

