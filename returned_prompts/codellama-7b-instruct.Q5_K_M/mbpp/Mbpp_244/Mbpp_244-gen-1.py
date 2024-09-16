```
def next_Perfect_Square(num):
    i = num + 1
    while i * i - num <= 0:
        i = i + 1
    return i * i
```
