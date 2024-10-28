
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    if not file_name[0].isalpha():
        return 'No'
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("example1.txt"))  # => 'Yes'
print(file_name_check("ex.ample.txt"))  # => 'No'
print(file_name_check("example.exe.dll"))  # => 'No'
print(file_name_check("ex@mpl$e.txt"))  # => 'No'
print(file_name_check("example123.txt"))  # => 'Yes'
print(file_name_check("ex@mple.dll"))  # => 'No'
print(file_name_check("exampl1e.dll"))  # => 'No'
print(file_name_check("example.txt.dll"))  # => 'No'
<jupyter_output>
Yes
No
Yes
No
No
No
Yes
No
No
No
<jupyter_text>
Problem 2
<jupyter_code>
