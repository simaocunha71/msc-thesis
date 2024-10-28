
```python
def fib4(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    fib = [0, 0, 2, 0]

    for i in range(4, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4])

    return fib[n]
```

The function `fib4` uses an iterative approach to compute the n-th element of the fib4 number sequence. It initializes a list `fib` with the first four elements of the sequence (`0, 0, 2, 0`) and then fills the rest of the list by adding the last four elements. This results in a list that contains the n-th element of the sequence at index `n`. The function then returns the n-th element of the sequence.

This function has a time complexity of O(n) because it iterates from 4 to `n` to fill the `fib` list, and each iteration takes constant time. It also has a space complexity of O(n) because it stores the entire `fib` list up to `n`.

This function can be used to compute the n-th element of the fib4 number sequence for any non-negative integer `n`.

Please note that this function uses recursion to compute the elements of the sequence, but it's a tail recursion. It's not a problem because the Python interpreter or compiler can optimize tail recursion by transforming it into a loop.

So, the function `fib4` is a tail-recursive function.
"""

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```

This function works by initializing a list `fib` with the first four elements of the sequence (`0, 0, 2, 0`), and then fills the rest of the list