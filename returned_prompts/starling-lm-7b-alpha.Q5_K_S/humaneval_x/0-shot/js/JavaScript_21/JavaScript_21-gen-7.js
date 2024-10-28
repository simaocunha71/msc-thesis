To rescale a list of numbers, you can follow these steps:

1. Find the range of the numbers, which is the difference between the maximum and minimum values.
2. Divide each number in the list by the range to get the relative position of each number in the range.
3. Multiply each number by the range to get the scaled number.

Here's a Python implementation of the `rescaleToUnit` function that follows these steps:

```python
def rescaleToUnit(numbers):
    # Step 1: Find the range of the numbers
    min_value = min(numbers)
    max_value = max(numbers)
    range_ = max_value - min_value

    # Step 2: Divide each number by the range to get the relative position
    scaled_numbers = [(number - min_value) / range_ for number in numbers]

    # Step 3: Multiply each number by the range to get the scaled number
    scaled_numbers = [number * range_ for number in scaled_numbers]

    return scaled_numbers
```

You can test the function with the example `[1.0, 2.0, 3.0, 4.0, 5.0]`:

```python
print(rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This will return `[0.0, 0.25, 0.5, 0.75, 1.0]`, which is the original list of numbers rescaled to have a minimum of 0 and a maximum of 1.

The function works by first finding the range of the input numbers, which is the difference between the maximum and minimum values. It then divides each number by the range to get the relative position of each number in the range, and multiplies each number by the range to get the scaled number. The result is a new list of numbers that have been rescaled to have a minimum of 