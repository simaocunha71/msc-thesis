
The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The first several Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, ...

Here's a function that returns the nth Fibonacci number:

```python
def fib(n):
    """Return n-th Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

You can test it with the examples given:

```python
print(fib(10))  # Prints: 55
print(fib(1))   # Prints: 1
print(fib(8))   # Prints: 21
```

As you can see, the function correctly computes the Fibonacci number for the given inputs.

In terms of time complexity, the function has a time complexity of O(n) since it calls itself twice for every input, and the depth of recursion is at most n.

In terms of space complexity, the function has a space complexity of O(n) since it uses a stack of depth n to store the recursive calls.














































