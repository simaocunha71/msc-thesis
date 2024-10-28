
def file_name_check(file_name):
    import re

    # The regular expression checks if there are no more than 3 digits, 
    # there is exactly one dot, the substring before the dot starts with a letter, 
    # and the substring after the dot is one of these: ['txt', 'exe', 'dll'].
    pattern = r"^[A-Za-z][A-Za-z0-9]{0,2}\.([tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL])$"

    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'


# Test cases
print(file_name_check("example.txt"))  #  Should return 'Yes'
print(file_name_check("1example.dll"))  #  Should return 'No'
print(file_name_check("ex.ample.dll"))  #  Should return 'No'
print(file_name_check("example.exe"))  #  Should return 'Yes'
print(file_name_check("ex@mpl.e"))  #  Should return 'No'
print(file_name_check("ex4mpl.txt"))  #  Should return 'Yes'
print(file_name_check("ex4mpl.exe"))  #  Should return 'No' (There are more than 3 digits)
print(file_name_check("exampl5.txt"))  #  Should return 'No' (There are more than 3 digits)
print(file_name_check("exampl.ex"))  #  Should return 'No' (Extension is not one of ['txt', 'exe', 'dll'])
print(file_name_check("exampl.dll"))  #  Should return 'Yes'
<jupyter_output>
Yes
No
No
Yes
No
Yes
No
No
No
Yes
<jupyter_text>
Task 4: Write a function that takes a string and a number, and rotates the characters in the string to the right by the number