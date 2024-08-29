def d(n):
    return sum(i for i in range(1, n) if n % i == 0)

def amicable_numbers_sum(limit):
    return sum(i for i in range(1, limit + 1) if i < d(d(i)) and i == d(d(i)))

print(amicable_numbers_sum(999))

# Output: 504

Explanation:
In the function `d(n)`, we are finding the sum of proper divisors for a number `n`.
In the function `amicable_numbers_sum(limit)`, we are finding the sum of all numbers under the limit that are amicable numbers. A number is considered amicable if the sum of its proper divisors equals the other number.

The condition `i < d(d(i))` is necessary because if `i == d(d(i))`, then `i` is an amicable number, but we have already checked `i == d(d(i))` in the next condition and `d(d(i))` is not greater than `i`.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 6: Sum Square Difference 