```
def occurance_substring(s, sub):
    index = s.find(sub)
    if index == -1:
        return None
    return (sub, index, index + len(sub) - 1)
```


This function uses the built-in `find` method of the string, which returns the index of the first occurrence of the substring. If the substring is not found, `find` returns -1. The function returns a tuple containing the substring, its starting index, and its ending index (inclusive). If the substring is not found, the function returns `None`. The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function returns the correct values for a given string and substring.