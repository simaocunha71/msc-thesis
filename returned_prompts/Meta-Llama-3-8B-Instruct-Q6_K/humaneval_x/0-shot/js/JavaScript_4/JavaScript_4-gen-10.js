Here is a Python function that calculates the Mean Absolute Deviation (MAD) around the mean of a given list of numbers:

```python
def meanAbsoluteDeviation(numbers):
    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)
```

This function first calculates the mean of the input list by summing up all the numbers and dividing by the length of the list. Then it calculates the absolute difference between each number and the mean, and sums up these differences. Finally, it returns the average of these differences, which is the Mean Absolute Deviation.

For example, if you call `meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])`, it will return `1.0`, which is the Mean Absolute Deviation around the mean of this dataset.