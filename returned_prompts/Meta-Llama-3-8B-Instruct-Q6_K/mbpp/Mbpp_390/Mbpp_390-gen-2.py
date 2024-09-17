```
def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]
```





The problem is asking you to create a function that takes a list of elements and a format string as input, and returns a new list where each element from the original list is formatted according to the given format string.

For example, if you have a list `[1, 2, 3, 4]` and a format string `'temp{0}'`, the function should return `['temp1', 'temp2', 'temp3', 'temp4']`.

The unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` helps to clarify the expected output.

Here is a Python solution that uses a list comprehension to achieve this:

```
def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]
```

This function uses the `format` method to replace `{0}` in the format string with each element from the list, and then returns the resulting list of formatted strings. The unit test confirms that this function works as expected.