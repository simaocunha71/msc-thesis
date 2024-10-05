Here is a Python function that calculates the Mean Absolute Deviation (MAD) of a list of numbers:

```python
def mean_absolute_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)
```

This function first calculates the mean of the input numbers. Then, it calculates the absolute difference between each number and the mean, and finally returns the average of these absolute differences.

For example, if you call `mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])`, it will return `1.0`, which is the correct result.

Here's how you can use this function:

```python
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```