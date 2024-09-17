```
def add_string(lst, fmt_str):
    return [fmt_str.format(i) for i in lst]
```
The function `add_string` takes a list `lst` and a format string `fmt_str` as input. It uses a list comprehension to apply the format string to each element in the list. The `format` method is used to replace `{0}` in the format string with the current element. The resulting list of formatted strings is then returned.

The unit test `assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']` ensures that the function works correctly. It checks that the function applies the format string `'temp{0}'` to the list `[1,2,3,4]` and returns the expected result `['temp1', 'temp2', 'temp3', 'temp4']`.