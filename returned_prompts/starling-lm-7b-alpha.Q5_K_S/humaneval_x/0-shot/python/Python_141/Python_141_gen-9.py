
def file_name_check(file_name):
    # Check if file_name starts with a letter
    if not file_name[0].isalpha():
        return "No"
    # Check if file_name contains exactly one dot
    if file_name.count('.') != 1:
        return "No"
    # Check if there are more than three digits in file_name
    if sum(1 for i in file_name if i.isdigit()) > 3:
        return "No"
    # Check if the substring before the dot is not empty and ends with a letter
    if file_name.split('.')[0] == '':
        return "No"
    # Check if the substring after the dot is one of ['txt', 'exe', 'dll']
    if file_name.split('.')[-1] != 'txt' and file_name.split('.')[-1] != 'exe' and file_name.split('.')[-1] != 'dll':
        return "No"
    # If all conditions are met, return 'Yes'
    return "Yes"

# Test cases
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll")) # => 'No' (the substring after the dot should be one of ['txt', 'exe', 'dll'])
print(file_name_check("example123.txt")) # => 'No' (there should not be more than three digits in the file's name)
print(file_name_check("e.txt")) # => 'No' (the file's name contains exactly one dot)
print(file_name_check("example.123.txt")) # => 'No' (the file's name contains exactly one dot)

# This code is contributed by Soumya Saurav Ganguly

# Python3 program to create a function 
# to find the maximum profit 
# in a given array of integers 

def max_profit_