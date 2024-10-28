
The Fibonacci sequence is the sequence of numbers in which each number after the first two is the sum of the two preceding ones. The first ten Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …

The Fibonacci sequence can be defined by the recurrence relation:

```
fib(n) = fib(n-1) + fib(n-2)
```

with initial terms:

```
fib(0) = 0
fib(1) = 1
```

To solve this problem, we can use a recursive function to calculate the `n`th Fibonacci number. However, this function has exponential time complexity, and it is not efficient to calculate large Fibonacci numbers directly.

Here's a Python function that calculates the `n`th Fibonacci number recursively:

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

The time complexity of this function is O(2^n) because for each recursive call, the function calls itself twice. As a result, the execution time of this function grows exponentially with the input size.

To optimize this function, we can use dynamic programming to store previously computed Fibonacci numbers. Here's an optimized version of the function with a time complexity of O(n):

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        fib_n = [0, 1, 1]
        while len(fib_n) < n + 1:
            fib_n.append(fib_n[-1] + fib_n[-2])
        return fib_n[n]
```

In this version of the function, we use a list `fib_n` to