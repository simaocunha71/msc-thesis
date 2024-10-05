
def file_name_check(file_name):
    if file_name[0].isalpha() and '.' in file_name and file_name.count('.') == 1 and file_name.split('.')[1] in ['txt', 'exe', 'dll'] and file_name.count('0')+file_name.count('1')+file_name.count('2')+file_name.count('3')+file_name.count('4')+file_name.count('5')+file_name.count('6')+file_name.count('7')+file_name.count('8')+file_name.count('9') <= 3:
        return "Yes"
    else:
        return "No"


# Alternative implementation:
def file_name_check(file_name):
    if re.match(r'^[a-zA-Z].*\.txt$'
                or r'^[a-zA-Z].*\.exe$'
                or r'^[a-zA-Z].*\.dll$', file_name):
        return "Yes"
    else:
        return "No"


# Alternative implementation using regular expressions:
import re

def file_name_check(file_name):
    if re.match(r'^[a-zA-Z].*\.txt$'
                or r'^[a-zA-Z].*\.exe$'
                or r'^[a-zA-Z].*\.dll$', file_name):
        return "Yes"
    else:
        return "No"


# Testing:
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)

























































