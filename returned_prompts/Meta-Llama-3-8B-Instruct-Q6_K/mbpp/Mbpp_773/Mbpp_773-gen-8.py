```
def occurance_substring(s, substring):
    if substring in s:
        start = s.index(substring)
        end = start + len(substring)
        return substring, start, end
    else:
        return None
```


The function `occurance_substring(s, substring)` takes two parameters, a string `s` and a substring. It checks if the substring is present in the string. If it is, it returns a tuple containing the substring, its start position and end position in the string. If the substring is not found, it returns `None`.

The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` ensures that the function works correctly. It checks that the function returns the substring 'python', its start position 0, and its end position 6 when searching for 'python' in the string 'python programming, python language'. 

The function uses the `in` operator to check if the substring is present in the string. If it is, it uses the `index` method to find the start position of the substring and calculates the end position by adding the length of the substring to the start position. If the substring is not found, the function returns `None`. 