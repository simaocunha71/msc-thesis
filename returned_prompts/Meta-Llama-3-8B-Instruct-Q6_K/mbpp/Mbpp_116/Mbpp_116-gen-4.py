The problem is asking you to write a function that takes a tuple of positive integers as input and returns a single integer. The integer is formed by concatenating the strings representation of the integers in the tuple.

Here is the Python solution for the problem:
```
def tuple_to_int(t):
    return int(''.join(map(str, t)))
```
This function uses the built-in `map` function to convert each integer in the tuple to a string, `join` to concatenate these strings together, and `int` to convert the resulting string back to an integer. 

The unit test `assert tuple_to_int((1,2,3))==123` ensures that the function works correctly. It checks if the output of the function when given the tuple `(1,2,3)` is equal to `123`. 

For example, if you call `tuple_to_int((1,2,3))`, the function will return `123`. This is because the string representation of the integers in the tuple is `'123'`, and when you convert this string back to an integer, you get `123`. 