```
def sum_squares(lst):
    return sum(math.ceil(num)**2 for num in lst)
```
Explanation:

This function uses a generator expression to square each number in the list, round it up to the nearest integer using `math.ceil()`, and then sum up all the squared numbers.

Here's a breakdown of how it works:

1. `math.ceil(num)**2`: This expression squares each number in the list and then rounds it up to the nearest integer using `math.ceil()`.
2. `for num in lst`: This is a generator expression that iterates over each number in the list.
3. `sum(...)`: This function sums up all the squared numbers returned by the generator expression.

By using `math.ceil()` instead of `round()`, we ensure that the result is always rounded up, as required in the problem statement. For example, `math.ceil(1.4)` returns `2`, whereas `round(1.4)` returns `1`.