def file_name_check(file_name):
    # Split the file name by '.' and check if there are exactly two parts
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    # Check if the first part starts with a letter from the latin alphabet
    if not parts[0][0].isalpha():
        return 'No'
    
    # Check if there are more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Check if the second part is one of the allowed extensions
    allowed_extensions = ['txt', 'exe', 'dll']
    if parts[1].lower() not in allowed_extensions:
        return 'No'
    
    return 'Yes'
    
# Test the function
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("abc.txt"))  # => 'Yes'
print(file_name_check("1234.txt"))  # => 'No'
print(file_name_check("example.1234"))  # => 'No'
print(file_name_check("example.txt.abc"))  # => 'No'
print(file_name_check("example"))  # => 'No'
print(file_name_check("example.txt."))  # => 'No'  # missing the extension
print(file_name_check("example.txtabc"))  # => 'No'  # no dot
print(file_name_check("example.txt123"))  # => 'No'  # more than three digits
print(file_name_check("example.txt1234"))  # => 'No'  # more than three digits
print(file_name_check("example.txtabc.txt"))  # => 'No'  # there are two dots
print(file_name_check("example.txt."))  # => 'No'  # missing the extension
print(file_name_check(".txt"))  # => 'No'  # the first part is empty
print(file_name_check("example..txt"))  # => 'No'  # there are two dots
print(file_name_check("example.txt."))  # => 'No'  # there are two dots
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("example.txt"))  # => '