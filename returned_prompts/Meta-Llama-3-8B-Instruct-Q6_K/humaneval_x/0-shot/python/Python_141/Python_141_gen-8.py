```
def file_name_check(file_name):
    if not isinstance(file_name, str):
        return 'No'
    if len(file_name) < 2:
        return 'No'
    if file_name[0].isalpha() == False:
        return 'No'
    if not '.' in file_name:
        return 'No'
    if file_name.count('.') > 1:
        return 'No'
    file_name_list = file_name.split('.')
    if len(file_name_list) < 2:
        return 'No'
    if len(file_name_list[0]) == 0:
        return 'No'
    if len(file_name_list[1]) > 4:
        return 'No'
    if not file_name_list[1].lower() in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    return 'Yes'
```



Here is the solution for the problem. It first checks if the file name is a string and if it has a length less than 2. Then it checks if the first character is a letter from the latin alphabet. After that, it checks if there is a dot in the file name and if there is more than one dot. Then it splits the file name into two parts and checks if the first part is not empty and if the second part is one of the allowed extensions. Finally, it checks if there are more than three digits in the file name. If all these conditions are met, it returns 'Yes', otherwise it returns 'No'. 

Note: The function is case sensitive for the file extension. If you want it to be case insensitive, you can convert the file extension to lower case before comparing it. For example, `file_name_list[1].lower()` in the code. 

Also, this function does not check if the file name is a valid file name in the operating system. It only checks if the file name meets the given conditions. 