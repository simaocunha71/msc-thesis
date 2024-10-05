```
def file_name_check(file_name):
    if len(file_name) == 0:
        return 'No'
    
    if not file_name[0].isalpha():
        return 'No'
    
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    if len(parts[0]) > 0 and not parts[0].isalpha():
        return 'No'
    
    if len(parts[1]) > 3 or not parts[1].isalpha():
        return 'No'
    
    allowed_extensions = ['txt', 'exe', 'dll']
    if parts[1].lower() not in allowed_extensions:
        return 'No'
    
    return 'Yes'
```


This function first checks if the file name is empty. If it is, the function returns 'No'. Then it checks if the first character of the file name is a letter. If it is not, the function returns 'No'. Then it checks if there is exactly one dot in the file name. If there is not, the function returns 'No'. Then it splits the file name into two parts using the dot as a separator. It checks if the first part is not empty and if it is not a letter. If it is not, the function returns 'No'. Then it checks if the second part is longer than three characters or if it is not a letter. If it is, the function returns 'No'. Finally, it checks if the second part is one of the allowed extensions. If it is not, the function returns 'No'. If the function has not returned 'No' by this point, it returns 'Yes'. 