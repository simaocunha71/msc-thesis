
def file_name_check(file_name):
    import re
    match = re.match(r'^[A-Za-z][A-Za-z0-9]{0,2}\.([tT][xX][tT])|([eE][xX][eE])|([dD][lL][lL])$', file_name)
    if match:
        return 'Yes'
    else:
        return 'No'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'  (the name should start with a latin alphapet letter)
print(file_name_check("examPle.txt"))  # => 'Yes'
print(file_name_check("examPle.dll"))  # => 'Yes'
print(file_name_check("examPle.exe"))  # => 'Yes'
print(file_name_check("exampletxt"))  # => 'No' (No dot)
print(file_name_check("example.pdf"))  # => 'No' (Unsupported file type)
print(file_name_check("examPle."))  # => 'No' (No file type)
print(file_name_check(".txt"))  # => 'No' (No file name)
print(file_name_check("exam_Ple.txt"))  # => 'No' (Underscores are not allowed)
print(file_name_check("examPle123.txt"))  # => 'No' (More than 3 digits)
print(file_name_check("ExamPle.txt"))  # => 'Yes'
<jupyter_output>
Yes
No
Yes
Yes
Yes
No
No
No
No
No
Yes
<jupyter_text>
Problem 4:
<jupyter_code>
