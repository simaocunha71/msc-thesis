```
def get_max_sum(n):
    memo = {1: 1}
    max_sum = 0

    def f(n):
        if n not in memo:
            if n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0:
                memo[n] = max(f(n//2) + f(n//3) + f(n//4) + f(n//5), n)
            else:
                memo[n] = max(f(n//2), f(n//3), f(n//4), f(n//5), n)
        return memo[n]

    max_sum = f(n)
    return max_sum
```


This function uses a memoization approach to store the results of subproblems in a dictionary `memo`. The function `f(n)` is defined to calculate the maximum sum for a given number `n`. The base case for the recursion is when `n` is 1, in which case the maximum sum is 1. For other numbers, the function calculates the maximum sum by considering the maximum sum of the numbers that can be divided evenly into `n`, and the number itself. The results are stored in the `memo` dictionary to avoid recalculating the same subproblem multiple times. The function returns the maximum sum for the given number `n`. The unit test `assert get_max_sum(60) == 106` is used to verify the correctness of the function.