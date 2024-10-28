
Here is a Python solution for the above problem:

```python
def SumToN(n):
    return (n * (n + 1)) / 2
```

You can use the `SumToN` function to calculate the sum of numbers from 1 to `n` by calling it with a specific value of `n`.

For example, if you want to calculate the sum of numbers from 1 to 30, you would call `SumToN(30)`. The function would then return the result, which is 465.

Similarly, if you want to calculate the sum of numbers from 1 to 100, you would call `SumToN(100)`. The function would return the result, which is 5050.

Here are some example usage of the `SumToN` function:

```python
print(SumToN(30))  # Output: 465
print(SumToN(100)) # Output: 5050
print(SumToN(5))   # Output: 15
print(SumToN(10))  # Output: 55
print(SumToN(1))   # Output: 1
```

The `SumToN` function uses a mathematical formula to calculate the sum of numbers from 1 to `n`. The formula is `(n * (n + 1)) / 2`. This formula is known as the arithmetic series formula, and it allows us to calculate the sum of an arithmetic series efficiently.

In the formula, `n` represents the last number in the series, and `(n + 1)` represents the number of terms in the series. By multiplying these two values and dividing by 2, we can obtain the sum of the series.

For example, if we want to calculate the sum of numbers from 1 to 30, we can substitute `n = 30` into the formula:

```
Sum = (30 * (30 + 1)) / 2
Sum = (30 * 31) / 2
Sum = 930 / 2
Sum = 465
```

So, the sum