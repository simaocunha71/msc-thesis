```
def occurance_substring(s, substr):
    pos = s.find(substr)
    if pos != -1:
        return substr, pos, pos + len(substr)
    else:
        return None
```



In this function, we use the `find` method of the string `s` to find the position of the substring `substr`. If the substring is found, we return a tuple containing the substring, its position, and its position plus the length of the substring. If the substring is not found, we return `None`. The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function works correctly.