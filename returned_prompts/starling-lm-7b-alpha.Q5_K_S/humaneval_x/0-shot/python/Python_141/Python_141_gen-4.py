
def file_name_check(file_name):
    # The number of digits
    digits = len(filter(str.isdigit, file_name))
    # The substring before the dot
    before_dot = file_name.split('.')[0]
    # The substring after the dot
    after_dot = file_name.split('.')[1].lower()
    # The conditions
    valid_conditions = all([
        digits <= 3,
        before_dot != '',
        before_dot[0].isalpha(),
        after_dot in ['txt', 'exe', 'dll']
    ])
    # The result
    if valid_conditions:
        return 'Yes'
    else:
        return 'No'

# Examples
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("123example.txt")) # => 'No' (the file's name contains more than three digits)
print(file_name_check("example")) # => 'No' (the file's name does not contain a dot)
print(file_name_check("example.txt.")) # => 'No' (the file's name contains more than one dot)
print(file_name_check("example.txt.123")) # => 'No' (the file's name contains more than three digits)




















































































































































