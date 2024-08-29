```python
def cal_sum(n):
    a = [3, 0, 2]
    p = [3, 0, 2]
    for i in range(3, n):
        a.append(a[i-2] + a[i-3])
        p.append(p[i-2] + p[i-3])
    return sum(p[:n])

print(cal_sum(9)) # 49
```

