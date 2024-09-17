You can use the `ast.literal_eval()` function to convert the string to an integer tuple. The `ast.literal_eval()` function safely evaluates a string containing a Python literal or container display.
Here is the solution:
```
import ast

def tuple_str_int(s):
    return ast.literal_eval(s)
```
This function will work as long as the string is a valid representation of a tuple of integers. If the string is not a valid representation of a tuple of integers, it will raise a `ValueError`. For example, if the string is `"(7, 8, 9.0)"`, it will raise a `ValueError` because `9.0` is not an integer. 

If you want to handle such cases, you can add error handling code to the function. For example:
```
import ast

def tuple_str_int(s):
    try:
        return ast.literal_eval(s)
    except ValueError:
        return None  # or some other default value
```
This function will return `None` if the string is not a valid representation of a tuple of integers. You can replace `None` with some other default value if you prefer. 

You can also use `eval()` function instead of `ast.literal_eval()` but it's not recommended because `eval()` can evaluate any Python expression, not just literals. It can pose a security risk if you're evaluating strings that come from an untrusted source. `ast.literal_eval()` is safer because it only evaluates literals, such as strings, bytes, numbers, tuples, lists, dicts, sets, and frozensets. It does not evaluate arbitrary Python code.  For example, `eval("os.system('rm -rf /')")` can delete all files on your system, but `ast.literal_eval("os")` will raise a `ValueError` because `os` is not a literal. 