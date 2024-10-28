def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    def is_valid(file_name):
        # Check for more than three digits
        if sum(c.isdigit() for c in file_name) > 3:
            return False
        # Check for exactly one dot
        if file_name.count('.') != 1:
            return False
        # Check for valid substring before dot
        dot_index = file_name.index('.')
        if not file_name[:dot_index].isalpha():
            return False
        # Check for valid substring after dot
        if file_name[dot_index + 1:] not in ['txt', 'exe', 'dll']:
            return False
        return True

    return 'Yes' if is_valid(file_name) else 'No'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)