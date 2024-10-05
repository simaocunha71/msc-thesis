The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).

The Fibonacci sequence is defined as follows:
fib(0) == 0
fib(1) == 1
fib(n) == fib(n-1) + fib(n-2)

The first few elements of the FibFib sequence are: 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
The first few elements of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

The FibFib sequence is a slight modification of the Fibonacci sequence, so we can re-use the Fibonacci sequence computation to compute the FibFib sequence.

Here's a function that efficiently computes the n-th element of the FibFib sequence using memoization:

```python
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
