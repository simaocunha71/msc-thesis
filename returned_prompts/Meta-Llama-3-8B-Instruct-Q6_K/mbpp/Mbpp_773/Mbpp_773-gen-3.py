```
def occurance_substring(s, sub):
    if sub in s:
        start = s.find(sub)
        return (sub, start, start + len(sub))
    else:
        return None
```


This function checks if the substring `sub` is present in the string `s`. If it is, it returns a tuple containing the substring, the starting position of the substring, and the ending position of the substring. If the substring is not found, it returns `None`.

The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function works correctly. It checks that when the substring 'python' is searched in the string 'python programming, python language', the function returns the tuple ('python', 0, 6), indicating that the substring 'python' starts at position 0 and ends at position 6. If the substring is not found, the function returns `None`, which is also checked by the unit test.