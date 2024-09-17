```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```





This function uses list comprehension to iterate over each string in the input list. For each string, it uses slicing with a step of -1 (`s[::-1]`) to reverse the string. The reversed strings are then returned as a new list.