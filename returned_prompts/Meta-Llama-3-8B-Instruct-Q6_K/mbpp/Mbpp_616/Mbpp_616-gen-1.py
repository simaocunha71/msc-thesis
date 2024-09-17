You can solve this problem by using a list comprehension in Python. The list comprehension will iterate over the indices of the two tuples and apply the modulo operation to the corresponding elements of the two tuples.

Here is the Python solution:
```
def tuple_modulo(t1, t2):
    return tuple(x % y for x, y in zip(t1, t2))
```
This function uses the built-in `zip` function to iterate over the indices of the two tuples. For each index, it calculates the modulo of the corresponding elements of the two tuples and returns the result as a tuple.

The unit test `assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)` ensures that the function works correctly. It checks if the result of the function is equal to the expected result `(0, 4, 5, 1)` when the input tuples are `(10, 4, 5, 6)` and `(5, 6, 7, 5)`. If the result is equal, the test passes; otherwise, it fails.