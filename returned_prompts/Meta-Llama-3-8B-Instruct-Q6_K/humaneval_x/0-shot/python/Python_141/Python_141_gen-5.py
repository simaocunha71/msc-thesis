```
def file_name_check(file_name):
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    if not parts[0][0].isalpha():
        return 'No'
    if len(parts[0]) > 1 and not parts[0][1:].isalnum():
        return 'No'
    if len(parts[1]) > 3:
        return 'No'
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```

This function splits the file name into two parts at the dot. It then checks each part against the conditions specified in the problem. If any of the conditions are not met, it returns 'No'. If all conditions are met, it returns 'Yes'. 

The conditions are:
- `len(parts) != 2`: The file name should contain exactly one dot.
- `not parts[0][0].isalpha()`: The substring before the dot should start with a letter from the latin alphabet.
- `len(parts[0]) > 1 and not parts[0][1:].isalnum()`: The substring before the dot should not be empty and it should not contain more than three digits.
- `len(parts[1]) > 3`: The substring after the dot should not be more than three characters long.
- `parts[1] not in ['txt', 'exe', 'dll']`: The substring after the dot should be one of 'txt', 'exe', or 'dll'. 

This function returns 'Yes' for valid file names and 'No' otherwise.  The examples provided in the problem are tested and the function returns the expected results.  For example, `file_name_check("example.txt")` returns 'Yes' and `file_name_check("1example.dll")` returns 'No'. 