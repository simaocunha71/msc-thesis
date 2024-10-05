Here is a Python function to compute the n-th element of the fibfib number sequence:
```
def fibfib(n: int):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
```
This function uses a simple iterative approach to compute the n-th element of the fibfib sequence. It initializes three variables `a`, `b`, and `c` to the first three elements of the sequence, and then iterates from `n=3` to `n`. In each iteration, it updates the values of `a`, `b`, and `c` to the next three elements of the sequence using the recurrence relation `a+b+c`. Finally, it returns the value of `c`, which is the n-th element of the sequence.

You can test this function using the provided test cases:
```
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```
This function has a time complexity of O(n), which is efficient for computing large values of n. However, for very large values of n, a more efficient approach might be needed.