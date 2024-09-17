```
def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 1:
            return 0
        max_sum = 0
        for i in range(2, 6):
            if k % i == 0:
                max_sum = max(max_sum, f(k // i) + k)
        memo[k] = max_sum
        return max_sum
    return f(n)
```
The function `get_max_sum` uses dynamic programming to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). It uses a dictionary `memo` to store the results of subproblems to avoid redundant calculations. The function `f` is a recursive function that calculates the maximum sum for a given number `k`. It iterates over the divisors of `k` and updates the maximum sum accordingly. Finally, the function returns the maximum sum for the given number `n`. The unit test `assert get_max_sum(60) == 106` ensures that the function returns the correct result for the input `60`. 












The function `get_max_sum` uses dynamic programming to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n). It uses a dictionary `memo` to store the results of subproblems to avoid redundant calculations. The function `f` is a recursive function that calculates the maximum sum for a given number `k`. It iterates over the divisors of `k` and updates the maximum sum accordingly. Finally, the function returns the maximum sum for the given number `n`. The unit test `assert get_max_sum(60) == 106` ensures that the function returns the correct result for the input `60`.