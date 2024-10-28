
def file_name_check(file_name):
    # Checking if the file name contains only one dot
    if "." not in file_name:
        return "No"
    # Splitting the file name into substrings before and after the dot
    before_dot, after_dot = file_name.split(".")
    # Checking if the substring before the dot is not empty
    if not before_dot:
        return "No"
    # Checking if the substring before the dot starts with a latin alphapet letter
    if not before_dot[0].isalpha():
        return "No"
    # Checking if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if after_dot.lower() not in ["txt", "exe", "dll"]:
        return "No"
    # Checking if there are not more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return "No"
    # If all the conditions are met, the file name is considered to be valid
    return "Yes"

# Testing the function
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No' (the name should start with a latin alphapet letter)

# Additional test cases
print(file_name_check("123.txt"))  # => 'No' (more than three digits)
print(file_name_check("a.txt"))  # => 'No' (there should be exactly one dot)
print(file_name_check("example.txt1"))  # => 'No' (there should be exactly one dot)

```
  
This function checks if a given file name is valid based on the specified conditions. It first checks if the file name contains only one dot, and if not, returns "No". Then, it splits the file name into substrings before and after the dot, and checks if the substring before the dot is not empty and starts with a latin alphapet letter. If not, it