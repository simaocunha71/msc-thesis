The function can be implemented in Python as follows:

```python
def truncate_number(number: float) -> float:
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

This function works by first converting the input number to an integer using the built-in `int()` function, which truncates the decimal part. Then it calculates the decimal part by subtracting the integer part from the original number. The result is the decimal part of the number. 

For example, if you call `truncate_number(3.5)`, the function will return `0.5`, which is the decimal part of the number. 

The function assumes that the input number is positive, as stated in the problem. If you want to handle negative numbers as well, you can modify the function to handle them separately. 

Note that the `int()` function rounds down to the nearest integer, so the decimal part will always be smaller than 1. 

The unit test `>>> truncate_number(3.5)` is a good example of how the function should work. It should return `0.5`, which is the decimal part of the number. 

The function can be tested with more examples to ensure it works correctly for all positive floating point numbers. 

The time complexity of this function is O(1), as it only involves a few simple arithmetic operations. The space complexity is also O(1), as it only uses a constant amount of space to store the integer part and decimal part. 