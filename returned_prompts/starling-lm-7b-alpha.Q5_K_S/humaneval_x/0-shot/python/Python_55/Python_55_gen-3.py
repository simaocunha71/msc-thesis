
The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

Here's a Python function that calculates the nth Fibonacci number:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

In this function, we start with `a` and `b` initialized to 0 and 1. Then, we use a loop to calculate the next Fibonacci number by adding the current two numbers together and updating `a` and `b` accordingly. Finally, we return the value of `a`, which is the nth Fibonacci number.

To test the function, you can use the doctest module in Python:

```python
from doctest import testmod
testmod()
```

This will run the provided test cases and verify that the function returns the correct Fibonacci numbers for the given inputs.

```python
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

You can replace the `# Your code here` comment in the provided solution with the code above, and it should work as expected.

Here's a sample interactive session with the function:

```python
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
```

As you can see, the function correctly calculates the Fibonacci numbers for the given inputs.

Note: The function uses a loop to calculate the Fibonacci number iteratively, which is a more efficient approach compared to using recursion. Recursion can be slow for large values of `n` due to the overhead of function calls, while iteration is faster and more efficient.

I