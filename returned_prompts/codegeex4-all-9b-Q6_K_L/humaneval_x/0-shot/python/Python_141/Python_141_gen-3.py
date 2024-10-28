def file_name_check(file_name):
    import re
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,2}\.(txt|exe|dll)$', file_name):
        return 'Yes'
    else:
        return 'No'

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("exampledll")) # => 'No' (the name should end with .txt, .exe or .dll)