```
def left_rotate(number, d):
    return (number << d) | (number >> (32-d))
```

