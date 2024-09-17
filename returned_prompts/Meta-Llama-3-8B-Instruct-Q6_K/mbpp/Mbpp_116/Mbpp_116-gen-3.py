The problem is asking to write a function that takes a tuple of positive integers as input and returns a single integer. The single integer is formed by concatenating the strings representing the integers in the tuple.

For example, if the input tuple is (1,2,3), the function should return 123.

Here is the Python solution for the problem:

```
def tuple_to_int(t):
    return int("".join(map(str, t)))
```

This function uses the built-in `join` method to concatenate the strings representing the integers in the tuple. The `map` function is used to convert each integer in the tuple to a string. The `int` function is then used to convert the resulting string back to an integer. 

The unit test `assert tuple_to_int((1,2,3))==123` ensures that the function works correctly for the given input. If the function returns the correct output for this input, it will pass the test. Otherwise, it will raise an AssertionError. 