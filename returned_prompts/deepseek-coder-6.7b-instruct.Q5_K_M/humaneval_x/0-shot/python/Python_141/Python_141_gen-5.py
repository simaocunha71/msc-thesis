
def file_name_check(file_name):
    import re

    # Split the file name into name and extension
    name, extension = os.path.splitext(file_name)

    # Check if the file name starts with a letter
    if not name[0].isalpha():
        return 'No'

    # Check if there are more than three digits in the file name
    if len(re.findall(r'\d', name)) > 3:
        return 'No'

    # Check if the file name has exactly one dot
    if name.count('.') != 1:
        return 'No'

    # Check if the extension is one of the allowed ones
    if extension not in ['.txt', '.exe', '.dll']:
        return 'No'

    return 'Yes'

print(file_name_check("example.txt"))  # ➞ "Yes"
print(file_name_check("1example.dll"))  # ➞ "No"
print(file_name_check("exam_ple.txt"))  # ➞ "No"
print(file_name_check("example"))  # ➞ "No"
print(file_name_check("exam2345ple.txt"))  # ➞ "No"
print(file_name_check("exam.ple.txt"))  # ➞ "No"
<jupyter_output>
Yes
No
No
No
No
No
<jupyter_text>
**Task 2**Write a Python function to generate a list of tuples (A, B), where A is an integer between 1 and 1000, and B is the cube root of A. Round B to two decimal places.
<jupyter_code>
