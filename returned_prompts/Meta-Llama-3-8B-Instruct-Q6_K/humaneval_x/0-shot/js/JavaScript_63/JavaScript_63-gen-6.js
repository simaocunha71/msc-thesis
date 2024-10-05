You can solve this problem using dynamic programming and memoization. Here is a Python solution:

```python
def fibfib(n):
    if n <= 1:
        return 0
    memo = {0: 0, 1: 0, 2: 1}
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]
```

In this solution, we first check if `n` is less than or equal to 1, and if so, return 0 because the first two elements of the fibfib sequence are 0. Then we create a dictionary `memo` to store the values of the fibfib sequence. We initialize the dictionary with the base cases: `fibfib(0) == 0`, `fibfib(1) == 0`, and `fibfib(2) == 1`.

Next, we use a loop to compute the values of the fibfib sequence from 3 to `n`. For each `i` in this range, we calculate the value of `fibfib(i)` as the sum of the values of `fibfib(i-1)`, `fibfib(i-2)`, and `fibfib(i-3)`. We store this value in the `memo` dictionary.

Finally, we return the value of `fibfib(n)` from the `memo` dictionary.

This solution has a time complexity of O(n) and a space complexity of O(n), making it efficient for large values of `n`. The memoization technique helps to avoid redundant calculations and reduces the time complexity.