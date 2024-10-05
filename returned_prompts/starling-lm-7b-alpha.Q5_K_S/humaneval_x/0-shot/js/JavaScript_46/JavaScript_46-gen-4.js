Here's a non-recursive function to compute the n-th element of the Fib4 number sequence:

```python
def fib4(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        sequence = [0, 0, 2, 0]
        for i in range(4, n + 1):
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3] + sequence[i-4])
        return sequence[n]
```

This function first checks if `n` is one of the first four elements of the sequence (0, 1, 2, or 3). If `n` is one of these, the function returns the corresponding value from the sequence. Otherwise, it initializes a list `sequence` with the first four elements of the sequence. Then, it uses a `for` loop to compute the next element of the sequence by adding the previous four elements, and appends this value to the end of the `sequence` list. Finally, the function returns the `n`-th element of the `sequence` list.

For example, if we call `fib4(5)`, the function will return 4, because the 5th element of the sequence is 4. Similarly, if we call `fib4(6)`, the function will return 8, and if we call `fib4(7)`, the function will return 14.

This solution is efficient because it only requires a single pass through the sequence to compute the `n`-th element, and it does not use recursion, which can be slow for large values of `n`.

```python
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
```

*/

```python
def fib4(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        sequence = [