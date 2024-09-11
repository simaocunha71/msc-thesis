```
def sum_average(n):
    if(n<=0):
        return (0,0)
    else:
        s = (n*(n+1))//2
        return (s,s/n)
```

The function `sum_average(n)` takes in an integer `n` and computes the sum and average of the first `n` natural numbers. If `n` is less than or equal to 0, the function returns a tuple containing the sum (`0`) and average (`0`). Otherwise, it computes the sum of the first `n` natural numbers using the formula `(n*(n+1))//2` and the average by dividing the sum by `n`.

The assertion `assert sum_average(10)==(55, 5.5)` checks if the function correctly computes the sum and average of the first 10 natural numbers. The expected output is a tuple containing `55` (the sum) and `5.5` (the average).

To use the function, you can call it with a desired value of `n`, like `sum_average(10)`, and it will return the corresponding sum and average.

Here's an example usage of the function:

```python
result = sum_average(10)
print(result)  # Output: (55, 5.5)
```

In this example, the function `sum_average(10)` is called, and the result `(55, 5.5)` is printed, confirming that the function correctly computes the sum and average of the first 10 natural numbers.

Note that the function assumes that `n` is a non-negative integer. If `n` is not a non-negative integer, the function may not produce the expected results.

Additionally, the function uses integer division (`//`) to ensure that the sum is an integer. If you prefer a floating-point average, you can use floating-point division (`/`) instead of integer division.

Overall, the function `sum_average(n)` provides a concise and efficient way to calculate the sum and average of the first `n` natural numbers.

