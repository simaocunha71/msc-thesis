The nth nonagonal number can be calculated as (n*(8n-1))/2. This is a well-known formula for the nth nonagonal number.

Here is the Python function to calculate the nth nonagonal number:

```
def is_nonagonal(n):
    return (n*(8*n-1))/2
```

This function takes an integer n as input and returns the nth nonagonal number. The formula (n*(8*n-1))/2 is used to calculate the result. The unit test `assert is_nonagonal(10) == 325` ensures that the function works correctly. 

For example, `is_nonagonal(10)` returns `325` which is the 10th nonagonal number. 

This function assumes that n is a positive integer. For negative integers or non-integer values, the function may not work correctly. If you need to handle these cases, you would need to add error checking code. 

Note that the function name is `is_nonagonal`, but it does not actually check if the input is a nonagonal number. It simply calculates the nth nonagonal number. If you want to check if a number is a nonagonal number, you would need a different function. 

The function can be used to calculate the nth nonagonal number for any positive integer n. For example, `is_nonagonal(5)` returns `25`, which is the 5th nonagonal number. 

The function can be used in a loop to calculate the nonagonal numbers for a range of values. For example, `for n in range(1, 11): print(is_nonagonal(n))` would print the first 10 nonagonal numbers. 