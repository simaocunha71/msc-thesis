The task is to write a function that converts a tuple string to an integer tuple. The tuple string is enclosed in parentheses and contains integers separated by commas. For example, the string "(7, 8, 9)" should be converted to the tuple (7, 8, 9).

Here is a Python solution for the problem:
```
def tuple_str_int(s):
    return tuple(int(x) for x in s[1:-1].split(','))
```
This function uses the `split` method to split the string into substrings separated by commas. Then it uses a generator expression to convert each substring to an integer using the `int` function. Finally, it converts the resulting iterator to a tuple using the `tuple` function.

The unit test `assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)` ensures that the function works correctly. It checks that the input string "(7, 8, 9)" is converted to the tuple (7, 8, 9). If the function is correct, this test will pass. If the function is incorrect, this test will fail and indicate the problem with the function.