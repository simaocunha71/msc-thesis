
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

    valid = True

    if len(file_name) < 5:                         # Check the length of the input string
        print('INVALID! The file\'s name is too short.')
        return False
    
    if not re.match('\w',file_name[0]):            #Check whether it starts with a Latin alphapet letter
        print('INVALID! The file\'s name does NOT start with a valid letter.')
        return False
    
    if len(re.findall("\d",file_name)) > 2:      # Check the length of digits in the input string
        print('INVALID! There should not be more than three digits ('0'-'9') in the file\'s name.')
        return False
    
    if len(re.findall("\d",file_name)) > 1:      # Check whether there is a dot '.' in the input string
         print('INVALID! The file\'s name does NOT contain exactly one dot.')
         return False

    filename_extension = re.findall(r'[.]',file_name)  
    
    if len(filename_extension) == 0