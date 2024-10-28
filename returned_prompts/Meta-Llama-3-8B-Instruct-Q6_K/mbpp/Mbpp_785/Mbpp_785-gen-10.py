```
def tuple_str_int(s):
    s = s.strip("()").replace(",", "")
    return tuple(int(i) for i in s.split())
```


This function takes a string `s` as input, removes the parentheses and commas, and then converts the remaining string to a tuple of integers. The unit test `assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)` confirms that the function works correctly. 

For example, if the input is `(7, 8, 9)`, the function will first remove the parentheses and commas to get `7869`. Then it will split this string into individual numbers and convert each number to an integer, resulting in the tuple `(7, 8, 9)`. 

The `strip` method is used to remove the parentheses, `replace` is used to remove the commas, and `split` is used to split the string into individual numbers. The `int` function is used to convert each number to an integer, and the `tuple` function is used to convert the list of integers to a tuple. 

This function assumes that the input string is a valid tuple of integers, i.e., it does not contain any non-integer characters or malformed integer values. If the input string is not a valid tuple of integers, the function will raise a ValueError. 

For example, if the input is `(7, 8, abc)`, the function will raise a ValueError because `abc` is not a valid integer. If the input is `(7, 8, 9, 10)`, the function will also raise a ValueError because it expects a tuple of three integers, not four. 

To handle these cases, you could add error checking code to the function. For example, you could use a regular expression to check that the input string matches the pattern of a tuple of integers, and raise a ValueError if it does not. You could also use a try-except block to catch any ValueError exceptions that are raised when converting the string to a tuple of integers. 

Here is an example of how you could add error checking code to the function:

```
import re

def tuple_str_int(s):
    s = s.strip("()").replace(",", "")
    if not re.match(r"\d+(,\s*\d+)*$", s):
        raise ValueError("Invalid tuple of integers")
    try:
        return tuple(int(i) for i in s.split())
    except ValueError as e