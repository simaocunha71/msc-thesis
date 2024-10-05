```
def eat(number, need, remaining):
    total = number
    if remaining >= need - number:
        total += need - number
        remaining -= need - number
    else:
        total += remaining
        remaining = 0
    return [total, remaining]
```