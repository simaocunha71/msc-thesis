Here is a Python implementation of the Mean Absolute Deviation (MAD) function:
```
def meanAbsoluteDeviation(numbers):
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad
```
Here's an explanation of the code:

1. Calculate the mean of the input numbers using the `sum` function and the length of the list.
2. Calculate the absolute difference between each number and the mean using a generator expression.
3. Calculate the average of these absolute differences using the `sum` function and the length of the list.
4. Return the MAD value.

You can test this function with the example input `[1.0, 2.0, 3.0, 4.0]`:
```
print(meanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```
Note that this implementation assumes that the input list is non-empty. If the list is empty, the function will raise a `ZeroDivisionError` when calculating the mean. You may want to add error handling to handle this case.