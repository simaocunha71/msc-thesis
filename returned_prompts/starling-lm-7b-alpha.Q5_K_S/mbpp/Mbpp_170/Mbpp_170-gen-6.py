"""
To find the sum of numbers within a range specified by two indices in a list, you can use the following function:

```python
def sum_range_list(numbers, start_index, end_index):
    # Check if the indices are valid
    if start_index < 0 or end_index > len(numbers) - 1:
        raise ValueError("Index out of range")
    # Calculate the sum of the numbers within the range
    total = sum(numbers[start_index: end_index+1])
    # Return the sum
    return total
```

Here's an example of how to use the function:
```python
numbers = [2,1,5,6,8,3,4,9,10,11,8,12]
start_index = 8
end_index = 10
sum_range = sum_range_list(numbers, start_index, end_index)
print(sum_range)  # Output: 29
```

In this example, the `sum_range_list` function is used to find the sum of the numbers in the `numbers` list between indices 8 and 10 (inclusive). The function checks if the indices are valid and then calculates the sum using slicing and the `sum` function. The result is returned as the `sum_range` variable, which is printed to verify the correctness of the function.
"""

def sum_range_list(numbers, start_index, end_index):
    # Check if the indices are valid
    if start_index < 0 or end_index > len(numbers) - 1:
        raise ValueError("Index out of range")
    # Calculate the sum of the numbers within the range
    total = sum(numbers[start_index: end_index+1])
    # Return the sum
    return total

numbers = [2,1,5,6,8,3,4,9,10,11,8,12]
start_index = 8
end_index = 10
sum_range = sum_range_list(numbers, start_index, end_index)
print(