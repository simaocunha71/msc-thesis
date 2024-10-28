```
def perfect_squares(start, end):
    perfect_squares = []
    for i in range(start, end+1):
        square_root = int(i ** 0.5)
        if square_root ** 2 == i:
            perfect_squares.append(i)
    return perfect_squares
```
The function `perfect_squares` takes two parameters, `start` and `end`, which are the start and end of the range of numbers. It returns a list of perfect squares within this range.

The function iterates over the range of numbers from `start` to `end` (inclusive). For each number `i` in this range, it calculates its square root using the exponentiation operator `**` with a power of 0.5. If the square root is an integer (i.e., if the square of the integer is equal to `i`), then `i` is a perfect square and it is added to the list `perfect_squares`.

Finally, the function returns the list `perfect_squares`.

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` ensures that the function works correctly. It checks that the function returns the list `[1, 4, 9, 16, 25]` when called with the arguments `1` and `30`. This list contains all perfect squares between 1 and 30. If the function is correct, this test will pass; otherwise, it will raise an AssertionError.