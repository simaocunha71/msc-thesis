```
def cube_Sum(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += i ** 3
    return result
```