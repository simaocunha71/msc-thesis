```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```


This function uses a list comprehension to iterate over each string in the input list. It uses Python's slice notation `s[::-1]` to reverse each string, and then returns the list of reversed strings. The unit test provided in the problem description ensures that the function works correctly.