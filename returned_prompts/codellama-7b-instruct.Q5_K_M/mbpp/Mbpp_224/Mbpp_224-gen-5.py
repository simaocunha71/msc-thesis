```
def count_set_bits(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count
```
