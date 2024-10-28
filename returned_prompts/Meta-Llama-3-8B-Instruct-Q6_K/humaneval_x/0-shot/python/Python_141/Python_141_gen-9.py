```
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    name, extension = file_name.split('.')
    if not name[0].isalpha() or not name.isalnum():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(c.isdigit() for c in name) > 3:
        return 'No'
    return 'Yes'
```


This function first checks if the file name has exactly one dot. If not, it returns 'No'. Then it splits the file name into the name and the extension. It checks if the name starts with a letter from the latin alphabet and is alphanumeric (contains only letters and numbers). If not, it returns 'No'. Then it checks if the extension is one of the allowed ones ('txt', 'exe', 'dll'). If not, it returns 'No'. Finally, it checks if the name contains more than three digits. If so, it returns 'No'. If all checks pass, it returns 'Yes'. 

The function uses the following methods:
- `split('.')`: splits the string into a list of two elements at the dot.
- `isalpha()`: checks if the string contains only letters (a-z and A-Z).
- `isalnum()`: checks if the string contains only letters and numbers.
- `isdigit()`: checks if the string contains a digit.
- `sum()`: sums up the number of digits in the string.
- `for c in name`: loops over each character in the string.
- `if condition: return 'No'`: returns 'No' if the condition is not met. 

The function uses these methods to check each condition in the problem statement. If any condition is not met, it returns 'No'. If all conditions are met, it returns 'Yes'. 