You can solve this problem by using the `format` function in Python. The `format` function is used to format a string. It can replace placeholders in the string with values.

Here is the solution:
```
def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]
```
This function takes a list `lst` and a format string `format_str` as input. It then uses a list comprehension to apply the format string to each element in the list. The `format` function is used to replace `{0}` in the format string with the current element in the list. The resulting list of formatted strings is then returned.

For example, if you call `add_string([1,2,3,4],'temp{0}')`, it will return `['temp1', 'temp2', 'temp3', 'temp4']`. This is because the format string `'temp{0}'` is replaced with `'temp1'` for the first element `1`, `'temp2'` for the second element `2`, and so on.