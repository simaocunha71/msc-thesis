
def file_name_check(file_name):
    # Check if the file name contains exactly one dot
    if "." not in file_name:
        return "No"
    # Split the file name into two parts: before and after the dot
    before_dot, after_dot = file_name.split(".")
    # Check if the part before the dot is not empty and is a latin alphapet letter
    if (len(before_dot) == 0 or not before_dot[0].isalpha()) or len(after_dot) != 3:
        return "No"
    # Check if the part after the dot is one of the allowed file types: ['txt', 'exe', 'dll']
    if after_dot != "txt" and after_dot != "exe" and after_dot != "dll":
        return "No"
    # If all the conditions are met, return "Yes"
    return "Yes"

# Example usage:
print(file_name_check("example.txt"))  # Output: 'Yes'
print(file_name_check("1example.dll"))  # Output: 'No'





def file_name_check(file_name):
    # Split the file name into two parts: before and after the dot
    before_dot, after_dot = file_name.split(".")
    # Check if the part before the dot is not empty and is a latin alphapet letter
    if (len(before_dot) == 0 or not before_dot[0].isalpha()) or len(after_dot) != 3:
        return "No"
    # Check if the part after the dot is one of the allowed file types: ['txt', 'exe', 'dll']
    if after_dot != "txt" and after_dot != "exe" and after_dot != "dll":
        return "No"
    # If all the conditions are met, return "Yes"
    return "Yes"

# Example usage:
print(file_name_check("example.txt"))  # Output: 'Yes'
print(file_name_check("1example.dll"))  # Output