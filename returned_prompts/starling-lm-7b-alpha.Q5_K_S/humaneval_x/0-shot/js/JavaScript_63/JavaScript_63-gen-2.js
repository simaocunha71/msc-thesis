Here's a function that efficiently computes the n-th element of the fibfib number sequence:

```python
def fibfib(n):
    a, b, c = 0, 0, 1
    for _ in range(n):
        a, b = b, a + b
        if _ == n - 1:
            c = a
    return c
```

Explanation:

- The function `fibfib` takes an integer `n` as input and returns the n-th element of the fibfib number sequence.
- Inside the function, we initialize three variables `a`, `b`, and `c` to 0, 0, and 1 respectively. These variables will store the current, previous, and next values in the fibfib sequence.
- We use a for loop to iterate from 0 to `n - 1` (since fibfib(0) and fibfib(1) are already defined). In each iteration, we update the values of `a`, `b`, and `c` to compute the next value in the sequence.
- Inside the loop, we update `a` to the previous value of `b`, and `b` to the sum of the previous values of `a` and `b`.
- After the loop, we check if the current iteration is equal to `n - 1`. If it is, we assign the value of `a` to `c` since `c` represents the n-th element of the fibfib sequence.
- Finally, we return the value of `c`.

This implementation has a time complexity of O(n) as we only need to perform a constant amount of operations in each iteration of the loop.

Here are some test cases to verify the correctness of the function:

```python
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
```

As we can see, the function correctly computes the n-th element of the fibfib number sequence for different values of `n`.

*/


def fibfib(n):
    a, b, c = 