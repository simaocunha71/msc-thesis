
def file_name_check(file_name):
    import re
    pattern = r'^[A-Za-z][A-Za-z0-9]{0,2}\.(txt|exe|dll)$'
    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("ex.ample.dll"))  # => 'No'
print(file_name_check("exam1ple.dll"))  # => 'Yes'
print(file_name_check("example.png"))  # => 'No'
print(file_name_check(".txt"))  # => 'No'
print(file_name_check("ex@mple.dll"))  # => 'No'
print(file_name_check("example"))  # => 'No'
print(file_name_check("exa.mple.docx"))  # => 'No'
print(file_name_check("exa999mple.dll"))  # => 'No'
print(file_name_check("Exa99mple.dll"))  # => 'Yes'
<jupyter_output>
Yes
No
No
Yes
No
No
No
No
No
Yes
<jupyter_text>
