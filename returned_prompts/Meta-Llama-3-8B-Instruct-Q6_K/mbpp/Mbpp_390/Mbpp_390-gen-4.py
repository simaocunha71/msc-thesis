```
def add_string(lst, fmt_str):
    return [fmt_str.format(i) for i in lst]
```
This function takes a list and a format string as inputs, and returns a new list where each element is the result of applying the format string to the corresponding element in the input list.

For example, if we call `add_string([1,2,3,4],'temp{0}')`, the output will be `['temp1', 'temp2', 'temp3', 'temp4']`.

The unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` ensures that the function works correctly. It checks that the output of the function is equal to the expected output when the input list is `[1,2,3,4]` and the format string is `'temp{0}'`. If the function is working correctly, the assertion will pass, and if not, it will raise an AssertionError.