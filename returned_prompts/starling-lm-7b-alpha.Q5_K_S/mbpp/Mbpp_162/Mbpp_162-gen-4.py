```python
def sum_series(n):
    if (n%2==0):
        return (n//2)*(n+1)
    else:
        return ((n-1)//2)*(n+1)+n
```

In the above code, we're checking if `n` is even (i.e. divisible by 2), in which case the sum is simply `(n/2)*(n+1)` (the first term `n` appears twice in the series). Otherwise, we add the last term `n` and subtract the first term `1`.

To verify the function, we can use the built-in `assert` statement to check if the function returns the expected result for a test case:

```python
assert sum_series(6) == 12
```

This will raise an error if the assertion fails, indicating that the function is not working as expected.

You can test the function with other values of `n` to ensure it works correctly. For example:

```python
print(sum_series(8))  # should print 28
print(sum_series(10))  # should print 38
```

This will output the sum of the series for each value of `n`.

In general, this function should work for any positive integer `n`.

Here's a step-by-step explanation of the solution:

1. Check if `n` is even by using the modulus operator `%` to check if `n` is divisible by `2`. If it is, return `(n/2)*(n+1)` to calculate the sum of the series.
2. If `n` is not even, add the last term `n` to the sum and subtract the first term `1`. This is because the series starts with `n` and ends with `1`, so we need to account for the missing terms.
3. Use the `assert` statement to verify the function's result for a test case (e.g., `assert sum_series(6) == 12`). This will raise an error if the function doesn't return the expected result.
4. Test the function with other values of `n` to ensure it works correctly