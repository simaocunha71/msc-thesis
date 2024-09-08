
Here is a python function that sums all amicable numbers from 1 to a specified number:

```python
def d(n):
    return sum(i for i in range(1, n) if n % i == 0)

def amicable_numbers_sum(n):
    return sum(i for i in range(1, n) if d(d(i)) == i and i != d(i))

assert amicable_numbers_sum(999) == 504
```

In this code, `d(n)` is a helper function that calculates the sum of proper divisors of a number `n`. The function `amicable_numbers_sum(n)` then applies `d(d(n)) == n` to all numbers from 1 to `n`. If the condition holds, the number is added to the sum.

Note: The condition `i != d(i)` is used to exclude the number itself from the sum, as it would not be an amicable pair.

If the input is 999, the function will add up all amicable numbers from 1 to 999 (inclusive). The function will return 504, which is the sum of 220 and 284.

Please note that this function can be slow for large inputs, because the function `d(n)` is called for each number from 1 to `n`. If you need to compute the sum of amicable numbers for a very large number, you may want to optimize the `d(n)` function or use a different approach.

The time complexity of this function is O(n^2), so it may be slow for large inputs.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
