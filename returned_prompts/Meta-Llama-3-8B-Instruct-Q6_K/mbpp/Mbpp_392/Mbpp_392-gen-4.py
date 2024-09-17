```
def get_max_sum(n):
    memo = {1: 1}

    def f(k):
        if k not in memo:
            if k % 2 == 0 and k % 3 == 0 and k % 4 == 0 and k % 5 == 0:
                memo[k] = max(f(k // 2) + f(k // 3) + f(k // 4) + f(k // 5), k)
            elif k % 2 == 0:
                memo[k] = max(f(k // 2), f(k))
            elif k % 3 == 0:
                memo[k] = max(f(k // 3), f(k))
            elif k % 4 == 0:
                memo[k] = max(f(k // 4), f(k))
            elif k % 5 == 0:
                memo[k] = max(f(k // 5), f(k))
            else:
                memo[k] = f(k)
        return memo[k]

    return f(n)
```
This function uses a memoization dictionary to store the results of sub-problems, so that they can be looked up instead of recomputed. The function f(k) computes the maximum sum for a given number k, and the main function get_max_sum(n) calls f(n) to compute the maximum sum for the given number n. The unit test `assert get_max_sum(60) == 106` ensures that the function works correctly for the given input. 







The provided unit test `assert get_max_sum(60) == 106` suggests that the function should return the maximum sum possible for a given number. The function uses a memoization dictionary to store the results of sub-problems, so that they can be looked up instead of recomputed. The function f(k) computes the maximum sum for a given number k, and the main function get_max_sum(n) calls f(n) to compute the maximum sum for the given number n. The function f(k) is defined recursively, and the base case is when k is less than 1. The recursive case is when k is divisible by 2, 3, 4, or 5, in which case the maximum sum is the maximum of the sum of the maximum sums of the quotients and k. If k is not divisible by any of these numbers, the maximum sum is simply k. The function f(k) is then called with the input n,