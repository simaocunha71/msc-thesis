def file_name_check(file_name):
    import re
    if re.search(r'\d', file_name).count() > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not re.search(r'[a-zA-Z]', file_name.split('.')[0]):
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))