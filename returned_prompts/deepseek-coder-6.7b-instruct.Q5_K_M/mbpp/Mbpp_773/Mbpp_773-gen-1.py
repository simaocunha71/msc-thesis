Here is the Python code to solve the problem:

```python
def occurance_substring(s, sub):
    position = s.find(sub)
    if position != -1:
        return (sub, position, position+len(sub))
    else:
        return None

print(occurance_substring('python programming, python language','python'))  # ('python', 0, 6)
```

In the above code, the function `occurance_substring` takes two arguments: `s` and `sub`. The function `find` is used to find the first occurrence of the substring `sub` in the string `s`. If `sub` is found, the function returns a tuple containing `sub`, the starting position of `sub` in `s`, and the ending position of `sub` in `s`. If `sub` is not found, the function returns `None`.

The function `find` returns the index of the first occurrence of the substring. If the substring is not found, it returns -1.

The starting and ending positions are calculated by adding the length of the substring to the position of the substring in the string.

The `print` statement calls the function with a string and a substring as arguments and prints the result.

The output of the `print` statement is `('python', 0, 6)`, which means that the substring 'python' is found at position 0 and ends at position 6 in the string.

Note: Python uses zero-based indexing, which means that the first character of the string is at position 0.

Please replace `'python programming, python language'` and `'python'` with your actual string and substring.
