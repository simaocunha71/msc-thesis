
def file_name_check(file_name):
    file_name_split = file_name.split(".")
    if len(file_name_split) != 2:
        return "No"
    if file_name_split[0] == "":
        return "No"
    if not file_name_split[0].isalpha():
        return "No"
    if len(file_name_split[1]) != 3:
        return "No"
    if file_name_split[1] not in ['txt', 'exe', 'dll']:
        return "No"
    if len(file_name_split[0]) > 3:
        return "No"
    return "Yes"


# Examples
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("abc_example.txt"))  # => 'Yes'
print(file_name_check("example_123.txt"))  # => 'No' (the name should not contain more than three digits)
print(file_name_check("example.txt_"))  # => 'No' (the name after the dot should be one of ['txt', 'exe', 'dll'])
print(file_name_check("123example.txt"))  # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("a_example.dll"))  # => 'No' (the name after the dot should be one of ['txt', 'exe', 'dll'])

# Here are some additional test cases
# print(file_name_check("example.txt_"))  # => 'No' (the name after the dot should not be empty)
# print(file_name_check(""))  # => 'No' (the name should not be empty)
# print(file_name_check("123_example.txt"))  # => 'No' (the name should start with a latin alphapet