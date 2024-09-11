```
def filter_oddnumbers(nums):
    """
    Filter odd numbers.

    >>> filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
    True
    """
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result
```

Here's a function that filters odd numbers from a list of numbers. It iterates through the numbers in the input list and appends each odd number to a result list.

The function uses the modulo operator `%` to check if a number is odd. If the remainder of dividing the number by 2 is not zero (`num % 2 != 0`), then the number is odd and is appended to the result list.

To test the function, you can use the provided assertion statement. It checks if the function correctly filters odd numbers from the input list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and returns `[1,3,5,7,9]`. If the assertion is True, it means the function is working correctly.

You can test the function with different input lists to verify its correctness.

Here's an example usage of the function:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_oddnumbers(numbers)
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
```

This will print the filtered odd numbers from the input list `numbers`.

Note that the function does not modify the original list and returns a new list containing only the odd numbers.

To use the function, simply call it with a list of numbers as the argument. The function will return a new list containing only the odd numbers from the input list.

I hope this helps! Let me know if you have any further