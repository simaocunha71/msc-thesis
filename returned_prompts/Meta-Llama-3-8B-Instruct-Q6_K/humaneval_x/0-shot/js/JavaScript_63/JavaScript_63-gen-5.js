Here is the Python implementation of the function to compute the n-th element of the fibfib number sequence:
```python
def fibfib(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a+b+c
    return c
```
The function uses the same approach as the Fibbonacci sequence, but with an additional term in the recurrence relation. The time complexity of this function is O(n), which is efficient for computing the n-th element of the fibfib sequence.

Note that the function uses a loop to compute the n-th element, but it's not necessary to store all the previous elements. The function only needs to keep track of the last three elements to compute the next element in the sequence. This is known as the "memoization" technique, which reduces the time complexity of the function.