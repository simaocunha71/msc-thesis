The problem can be solved by creating a function that calculates the nth element of the fibfib sequence. The function can use memoization to store previously calculated values and avoid redundant calculations.

Here is the solution:

```
def fibfib(n: int):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo = {1: 0, 2: 1}
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
```

This function uses a dictionary `memo` to store previously calculated values. It first checks if the input `n` is less than or equal to 1, in which case it returns 0. If `n` is 2, it returns 1. Otherwise, it calculates the value of `fibfib(n)` by summing up the values of `fibfib(n-1)`, `fibfib(n-2)`, and `fibfib(n-3)`, and stores it in the `memo` dictionary. Finally, it returns the value of `fibfib(n)` from the `memo` dictionary.

This function has a time complexity of O(n) and a space complexity of O(n), making it efficient for calculating the nth element of the fibfib sequence.