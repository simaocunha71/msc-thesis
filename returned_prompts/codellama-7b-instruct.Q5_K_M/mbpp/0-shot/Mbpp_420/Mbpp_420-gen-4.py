```
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i ** 3
    return sum
```
