Here's a possible solution using Python:

```python
def get_odd_collatz(n):
    sequence = []
    num = n

    while num != 1:
        if num % 2 == 1:
            sequence.append(num)
            num = 3 * num + 1
        else:
            num = num // 2

    return sorted(sequence)
```

This Python