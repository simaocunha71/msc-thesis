```
def find_solution(a, b, n):
    d = a * b
    if n % d != 0:
        return None
    x = n * b // d
    y = n * a // d
    return (x, y)
```

