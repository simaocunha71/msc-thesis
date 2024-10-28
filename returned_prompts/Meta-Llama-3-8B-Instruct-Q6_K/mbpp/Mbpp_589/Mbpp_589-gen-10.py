```
def perfect_squares(a, b):
    return [i ** 2 for i in range(int(a ** 0.5), int(b ** 0.5) + 1)]
```
This function generates a list of perfect squares between two given numbers `a` and `b`. It uses a list comprehension to iterate over the range of numbers from the square root of `a` to the square root of `b` (inclusive), and then squares each number to get the perfect squares. The result is a list of perfect squares between `a` and `b`.

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` confirms that the function works correctly. It checks that the function returns the list `[1, 4, 9, 16, 25]` when called with `a=1` and `b=30`. This list contains the perfect squares between 1 and 30.