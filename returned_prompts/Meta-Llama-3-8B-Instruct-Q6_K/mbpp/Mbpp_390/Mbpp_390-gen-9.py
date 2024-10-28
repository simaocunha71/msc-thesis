```
def add_string(lst, format_str):
    return [format_str.format(i) for i in lst]
```
This function uses list comprehension to apply the given format string to each element in the list. The `format_str.format(i)` expression replaces `{0}` with the value of `i` in each iteration. The resulting list of formatted strings is returned. The provided unit test demonstrates the expected behavior of this function. For example, when called with the input list `[1, 2, 3, 4]` and the format string `'temp{0}'`, the function should return the list `['temp1', 'temp2', 'temp3', 'temp4']`. 