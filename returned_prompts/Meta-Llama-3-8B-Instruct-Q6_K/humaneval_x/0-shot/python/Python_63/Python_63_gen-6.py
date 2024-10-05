This problem can be solved using a memoization technique. The idea is to store the results of expensive function calls and return the cached result when the same inputs occur again. Here is a Python solution using a dictionary to store the memoized results:
```
def fibfib(n: int):
    if n <= 1:
        return 0
    memo = {1: 0, 2: 1}
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]
```
This function first checks if `n` is less than or equal to 1, in which case it returns 0. Then it initializes a dictionary `memo` with the base cases `fibfib(1)` and `fibfib(2)`. It then iterates from 3 to `n` and computes each `fibfib(i)` by adding the previous three values in the sequence. Finally, it returns the `n`-th element of the sequence.

This function has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of `n`. You can test it with the given examples:
```
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24
```
Note that this function uses a dictionary to store the memoized results, which makes it more efficient than a recursive solution that computes the same values multiple times. However, for very large values of `n`, a more advanced optimization technique such as dynamic programming or matrix exponentiation might be needed.