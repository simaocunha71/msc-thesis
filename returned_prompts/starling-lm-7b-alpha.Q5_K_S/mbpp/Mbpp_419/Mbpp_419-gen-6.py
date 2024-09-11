To round and sum a list of numbers, you can follow these steps:

1. Define a function called `round_and_sum` that takes a list of numbers as an argument.
2. Use a list comprehension to round each number in the list using the `round()` function.
3. Use the `sum()` function to calculate the sum of the rounded numbers.
4. Multiply the sum by the length of the original list using the `len()` function.
5. Return the result.
6. Test the function by calling it with a sample list of numbers and asserting that the result matches the expected output.

Here's an example implementation in Python:

```python
def round_and_sum(nums):
    rounded_nums = [round(num) for num in nums]
    total_sum = sum(rounded_nums)
    length = len(nums)
    result = total_sum * length
    return result

assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
```

In this code, the `round_and_sum` function takes a list of numbers `nums` as an argument. It uses a list comprehension to round each number in the list using the `round()` function. The rounded numbers are stored in the `rounded_nums` list.

The `sum()` function is then used to calculate the sum of the rounded numbers stored in `rounded_nums`. The length of the original list `nums` is calculated using the `len()` function and stored in the `length` variable.

Finally, the total sum `total_sum` is multiplied by the length `length` to obtain the result. The function returns this result.

The `assert` statement is used to verify that the result of calling the `round_and_sum` function with the sample list `[22.4, 4.0, -16.22, -9.10, 11.00, -12.