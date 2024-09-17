```
def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1)]
```
This function generates a list of perfect squares between the given start and end numbers. It does this by iterating over the range of numbers from the square root of the start to the square root of the end (inclusive), squaring each number, and adding it to the list.

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` helps to clarify the problem by providing a specific example of the expected output.

For example, calling `perfect_squares(1, 30)` would return the list `[1, 4, 9, 16, 25]`, which are the perfect squares between 1 and 30. The function works by iterating over the range of numbers from the square root of 1 (which is 1) to the square root of 30 (which is 5.5), and squaring each number to add it to the list. The `int` function is used to convert the square roots to integers, so that the range starts from the integer square root of the start number and ends at the integer square root of the end number. The `+1` is used to include the end number in the range, since the range function in Python is exclusive of the end value. 