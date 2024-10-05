Here is the Python code that fulfills the requirements:

```Python
import re

def FileNameCheck(file_name):
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not re.match('^[a-zA-Z].*', file_name[:file_name.index('.')]):
        return 'No'
    if file_name[file_name.index('.') + 1:].lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```

Here is how the function works:

1. It first checks if there are more than 3 digits in the file name. If there are, it returns 'No'.

2. Then it checks if the file name contains exactly one dot. If it doesn't, it returns 'No'.

3. Next, it checks if the substring before the dot starts with a latin alphapet letter. If it doesn't, it returns 'No'.

4. Finally, it checks if the substring after the dot is one of the valid extensions ('txt', 'exe', 'dll'). If it's not, it returns 'No'. If all the checks pass, it returns 'Yes'. 

This function uses the `re` module for regular expressions to simplify the checks. The `re.findall(r'\d', file_name)` function finds all the digits in the file name, and the `re.match('^[a-zA-Z].*', file_name[:file_name.index('.')])` function checks if the substring before the dot starts with a latin alphapet letter. The `file_name.count('.')` function counts the number of dots in the file name. The `file_name.index('.')` function finds the index of the dot in the file name. The `file_name[file_name.index('.') + 1:].lower()` function gets the substring after the dot and converts it to lowercase. The `in` operator checks if the substring is in the list of valid extensions.  If any of these checks fail, the function returns 'No'. If all the checks pass, it returns 'Yes'. 