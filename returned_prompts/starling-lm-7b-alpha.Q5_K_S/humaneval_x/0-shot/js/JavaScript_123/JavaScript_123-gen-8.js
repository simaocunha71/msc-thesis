In Python, you can solve this problem with the following code:

```python
def getOddCollatz(n):
    collatz = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
            collatz.append(n)
    return sorted(collatz)
```

Here's an explanation of the solution:

1. The function `getOddCollatz` takes a positive integer `n` as input.
2. It