def file_name_check(file_name):
    import re
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,2}\.exe|\.dll|\.txt$', file_name):
        return 'No'
    else:
        return 'Yes'

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.dll")) # => 'Yes'
print(file_name_check("example.TXT")) # => 'Yes'
print(file_name_check("example.tx")) # => 'No'
print(file_name_check("example.txT")) # => 'No'
print(file_name_check("example.txT.exe")) # => 'No'
print(file_name_check("example.txT.exe")) # => 'No'
print(file_name_check("example.txT.exe")) # => 'No'