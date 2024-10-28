```
def odd_values_string(s):
    return s[::2]
```


This function uses Python's slice notation to create a new string that includes every other character from the original string, starting from the first character (index 0). The `::2` slice means "start at the beginning of the string and end at the end, move forward in steps of 2". So, the function effectively removes the characters at odd index values. The unit test `assert odd_values_string('abcdef') == 'ace'` confirms this behavior. 