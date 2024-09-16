```
def left_rotate(n: int, d: int) -> int:
    return (n << d) | (n >> (32 - d))
```
