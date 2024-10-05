    if not isinstance(file_name, str):
        return 'No'

    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    if not parts[0][0].isalpha():
        return 'No'

    for char in parts[0][1:]:
        if char.isdigit() and parts[0][1:].count(char) > 1:
            return 'No'

    if len(parts[0][1:]) > 3:
        return 'No'

    if not parts[1] in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'  # file_name is valid
# test
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example1.txt"))  # => 'Yes'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example.dll"))  # => 'Yes'
print(file_name_check("example1.exe"))  # => 'Yes'
print(file_name_check("example123.txt"))  # => 'No'
print(file_name_check("example.txt1"))  # => 'No'
print(file_name_check("example.txt123"))  # => 'No'
print(file_name_check("example"))  # => 'No'
print(file_name_check("example1"))  # => 'No'
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("example.txt1"))  # => 'No'
print(file_name_check("example.txt123"))  # => 'No'
print(file_name_check("example.exe1"))  # => 'No'
print(file_name_check("example.exe123"))  # => 'No'
print(file_name_check("example.dll1"))  # => 'No'
print(file_name_check("example.dll123"))  # => 'No'
print(file_name_check("example123.txt"))  # => 'No'
print(file_name_check("example123.exe"))  # => 'No'
print(file_name_check("example123.dll"))  # => 'No'
print(file_name_check("example1.txt"))  # => 'No'
print(file_name_check("example1.exe"))  # => 'No'
print(file_name_check("example1.dll"))  # => 'No'
print(file_name_check("example2.txt"))  # => 'No'
print(file_name