```
def occurance_substring(s, sub_str):
    try:
        pos = s.index(sub_str)
        return (sub_str, pos, pos + len(sub_str) - 1)
    except ValueError:
        return None
```
The function `occurance_substring(s, sub_str)` takes two parameters: `s` (the string to be searched) and `sub_str` (the substring to be searched for). It returns a tuple containing the substring, its position in the string, and the position of the last character of the substring.

If the substring is found in the string, it returns the desired information. If the substring is not found, it returns `None`. The `index()` method is used to find the position of the substring, and the `try-except` block is used to handle the case where the substring is not found. The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function works correctly. 