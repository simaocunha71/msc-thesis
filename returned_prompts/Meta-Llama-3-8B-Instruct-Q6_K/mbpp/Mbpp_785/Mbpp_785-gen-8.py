You can use the built-in `ast.literal_eval()` function to convert a string representation of a tuple to a tuple of integers. Here is the solution:

```
import ast

def tuple_str_int(s):
    return ast.literal_eval(s)
```

This function works by taking a string `s` as input, and then using `ast.literal_eval(s)` to convert it to a tuple of integers. The `ast.literal_eval()` function is a safe way to evaluate a string as a Python literal, such as a tuple. It only evaluates literals, not arbitrary Python code, which makes it safe to use with untrusted input.

The unit test `assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)` ensures that the function works correctly. It checks that the output of the function is the same as the expected output, which is `(7, 8, 9)`. If the function is implemented correctly, this test will pass. If the function is not implemented correctly, this test will fail, indicating that there is a bug in the function.