To solve this problem, we can use a dynamic programming approach. We'll use a boolean array to store whether a certain number can be represented as the sum of exactly 4 positive even numbers. We'll initialize this array with false for all numbers. Then we'll iterate over this array and update it according to the following rules:

1. If a number is represented as the sum of exactly 4 positive even numbers, the number itself must be even (divisible by 2) and the sum of 4 even numbers is also even (which means the number is also even). So if `dp[i]` is true and `i` is even, then `dp[i]` will be set to true.
2. If a number is represented as the sum of exactly 4 positive even numbers, the number itself must be odd (not divisible by 2). This is because if `i` is odd, then the sum of 4 even numbers will be odd, and an odd number cannot be represented as the sum of exactly 4 positive even numbers. So if `dp[i]` is true and `i` is odd, then `dp[i]` will be set to false.
3. If a number is represented as the sum of exactly 4 positive even numbers, then all the even numbers that add up to this number must be smaller than the number itself. So if `dp[i]` is true, then `dp[i-2]` will be set to true.
4. If a number is represented as the sum of exactly 4 positive even numbers, then all the even numbers that add up to this number must be odd. This is because the sum of 4 even numbers is always even, and an even number cannot be represented as the sum of exactly 4 positive even numbers. So if `dp[i]` is true, then `dp[i-4]` will be set to true.

Finally, we'll return the value of `dp[n]`.

Here's a Python implementation of the above approach:

```python
def is_equal_sum_even(n: int) -> bool:
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(2, n + 1):
        if dp[i - 2] or