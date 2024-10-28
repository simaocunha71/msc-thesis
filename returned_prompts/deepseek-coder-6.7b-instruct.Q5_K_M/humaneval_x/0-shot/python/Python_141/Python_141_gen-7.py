
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if not name or not name[0].isalpha() or not extension in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(c.isdigit() for c in name) > 3:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' 
print(file_name_check("example1.txt"))  # => 'Yes'
print(file_name_check("ex.ample1.txt"))  # => 'No' 
print(file_name_check("example.txt.exe"))  # => 'No'
print(file_name_check("example1234.txt"))  # => 'No'
print(file_name_check("e1.txt"))  # => 'No'
print(file_name_check(".txt"))  # => 'No'
print(file_name_check("example."))  # => 'No'
print(file_name_check("example"))  # => 'No'
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("example123.dll"))  # => 'Yes'
<jupyter_output>
Yes
No
Yes
No
No
No
No
No
No
Yes
Yes
<jupyter_text>
