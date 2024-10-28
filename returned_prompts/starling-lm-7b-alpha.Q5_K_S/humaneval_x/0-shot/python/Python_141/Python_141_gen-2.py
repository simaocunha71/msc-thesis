
def file_name_check(file_name):
    if len([i for i in file_name if i.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if file_name[0].isalpha():
        first_part = file_name[:file_name.index('.')]
    else:
        return 'No'
    if file_name[file_name.index('.'):].lower() in ['txt', 'exe', 'dll']:
        return 'Yes'
    else:
        return 'No'


# Test Cases:
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.txt1")) # => 'No' (more than 3 digits)
print(file_name_check("example1.txt")) # => 'No' (more than 3 digits)
print(file_name_check("exampl1.txt")) # => 'No' (more than 3 digits)
print(file_name_check("1example.txt")) # => 'No' (name should start with alphabet)
print(file_name_check("exampl.txt")) # => 'No' (the name should contain exactly one dot)
print(file_name_check("exampl.txt.")) # => 'No' (the name should contain exactly one dot)
print(file_name_check("example.txt.")) # => 'No' (the name should contain exactly one dot)
print(file_name_check("example.txtdll")) # => 'No' (the name should contain exactly one dot)
print(file_name_check("example.txt..exe")) # => 'No' (the name should contain exactly one dot)













































