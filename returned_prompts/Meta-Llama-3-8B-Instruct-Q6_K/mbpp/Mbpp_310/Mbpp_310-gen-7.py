```
def string_to_tuple(s):
    return tuple(s)
```


In this problem, we need to write a function that converts a given string into a tuple of characters. The function should take a string as input and return a tuple where each character in the string is a separate element in the tuple.

For example, if the input string is "python 3.0", the output should be ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0').

The unit test `assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')` helps to clarify the expected behavior of the function.

The solution to this problem is simple. We can use the built-in `tuple()` function in Python, which converts an iterable (such as a string) into a tuple. So, the function `string_to_tuple(s)` can be defined as `return tuple(s)`. This function takes a string `s` as input, converts it into a tuple using the `tuple()` function, and returns the resulting tuple.