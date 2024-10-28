```
def file_name_check(file_name):
    if '.' not in file_name:
        return 'No'
    before_dot, after_dot = file_name.rsplit('.', 1)
    if not before_dot[0].isalpha():
        return 'No'
    if len([char for char in before_dot if char.isdigit()]) > 3:
        return 'No'
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
```


Explanation:
- The function takes a string representing a file's name.
- It checks if the file's name contains exactly one dot '.'. If not, it returns 'No'.
- It splits the file's name into two parts: the substring before the dot and the substring after the dot.
- It checks if the substring before the dot starts with a letter from the latin alphabet. If not, it returns 'No'.
- It counts the number of digits in the substring before the dot. If there are more than three digits, it returns 'No'.
- It checks if the substring after the dot is one of the allowed extensions ['txt', 'exe', 'dll']. If not, it returns 'No'.
- If all conditions are met, it returns 'Yes'.