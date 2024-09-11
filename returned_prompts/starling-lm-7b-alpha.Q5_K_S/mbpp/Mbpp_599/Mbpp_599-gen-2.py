```
def sum_average(n):
    sum_n = (n * (n + 1)) / 2
    average = sum_n / float(n)
    return sum_n, average
```

Here's a Python function to find the sum and average of the first n natural numbers. The function `sum_average(n)` takes an integer n as an argument. It calculates the sum of the first n natural numbers using the formula `(n * (n + 1)) / 2`. The average is calculated by dividing the sum by the number of terms, n. The function returns a tuple containing the sum and the average.

The assertion `assert sum_average(10)==(55, 5.5)` is used to verify that the function correctly calculates the sum and average of the first 10 natural numbers. The expected result is a tuple `(55, 5.5)`.

To use the function, simply call it with the desired value of n as an argument. For example, `sum_average(10)` will return the sum and average of the first 10 natural numbers.

Here's an example usage of the function:

```python
result = sum_average(10)
print(result)  # Output: (55, 5.5)
```

This will print the sum and average of the first 10 natural numbers, which are 55 and 5.5, respectively.

```python
def sum_average(n):
    sum_n = (n * (n + 1)) / 2
    average = sum_n / float(n)
    return sum_n, average
```

This function calculates the sum and average of the first n natural numbers using the provided formula. It takes an integer `n` as an argument and returns a tuple containing the sum and average.

The assertion `assert sum_average(10)==(55, 5.5)` is used to verify that the function correctly calculates the sum and average of the first 10 natural numbers. The expected result is a tuple `(55, 5.5)`.

To use the function,