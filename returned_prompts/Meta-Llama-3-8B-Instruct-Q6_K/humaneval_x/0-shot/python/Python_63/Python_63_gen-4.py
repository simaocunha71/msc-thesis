The problem is to create a function that calculates the nth element of the FibFib number sequence. The FibFib sequence is defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

Here is a Python solution using memoization to store previously computed values:

```
def fibfib(n: int):
    if n <= 1:
        return 0
    memo = {1: 0, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]
```

This function works by first checking if n is less than or equal to 1, in which case it returns 0. Then, it creates a dictionary called memo to store previously computed values. It iterates from 3 to n (inclusive), and for each i, it calculates the value of fibfib(i) by adding the values of fibfib(i-1), fibfib(i-2), and fibfib(i-3). Finally, it returns the value of fibfib(n).

The time complexity of this function is O(n), as it needs to iterate from 3 to n to compute the nth element. The space complexity is also O(n), as it needs to store the values of fibfib(i) for i from 1 to n in the memo dictionary.