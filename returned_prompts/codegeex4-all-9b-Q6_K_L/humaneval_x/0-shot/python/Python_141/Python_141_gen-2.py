def file_name_check(file_name):
    import re
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not re.match(r'^[a-zA-Z]', file_name.split('.')[0]):
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.txty")) # => 'No' (more than one dot)
print(file_name_check("example.txty.dll")) # => 'No' (more than one dot)
print(file_name_check("example.txt.exe")) # => 'No' (more than one dot)
print(file_name_check("example.txtyexe")) # => 'No' (more than one dot)
print(file_name_check("example.txtyexe.dll")) # => 'No' (more than one dot)
print(file_name_check("example.txtyexe.dll.exe")) # => 'No' (more than one dot)