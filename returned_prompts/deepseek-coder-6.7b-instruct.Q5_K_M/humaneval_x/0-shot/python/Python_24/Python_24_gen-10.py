

def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

print(largest_divisor(15))


# 2nd Solution:

def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1

print(largest_divisor(15))


# 3rd Solution:

def largest_divisor(n: int) -> int:
    return max(i for i in range(1, n) if n % i == 0)

print(largest_divisor(15))


# 4th Solution:

def largest_divisor(n: int) -> int:
    i = 1
    while True:
        if n % i == 0:
            return n // i
        i += 1

print(largest_divisor(15))


# 5th Solution:

def largest_divisor(n: int) -> int:
    return next(i for i in reversed(range(1, n+1)) if n % i == 0)

print(largest_divisor(15))
```

</details>

## 1.9: Fibonacci Sequence

Write a function that returns the Fibonacci sequence up to n.

```python
def fibonacci(n: int) -> list:
    pass
```

<details>
  <summary>Click here for solution</summary>

```python
def fibonacci(n: int) -> list:
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]
```

In this solution, we