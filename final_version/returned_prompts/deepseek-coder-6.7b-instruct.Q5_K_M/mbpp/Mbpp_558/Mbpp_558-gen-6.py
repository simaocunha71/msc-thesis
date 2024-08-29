```python
def digit_distance_nums(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    return sum(abs(int(a) - int(b)) for a, b in zip(s1, s2))

print(digit_distance_nums(1,2))  # 1
```

