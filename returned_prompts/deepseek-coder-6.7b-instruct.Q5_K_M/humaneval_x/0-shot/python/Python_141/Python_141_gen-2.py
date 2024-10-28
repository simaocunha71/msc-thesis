
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if not name[0].isalpha() or name.isnumeric() or len(name) == 0:
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(i.isdigit() for i in file_name) > 3:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt"))  # 应该返回 "Yes"
print(file_name_check("1example.dll"))  # 应该返回 "No"
print(file_name_check("example1.dll"))  # 应该返回 "Yes"
print(file_name_check("example.dll.txt"))  # 应该返回 "No"
print(file_name_check("example1234.dll"))  # 应该返回 "No"
print(file_name_check("example1..dll"))  # 应该返回 "No"
print(file_name_check("example.1234"))  # 应该返回 "No"
print(file_name_check("ex.ample1.dll"))  # 应该返回 "No"
print(file_name_check("ex.ample.1234.dll"))  # 应该返回 "No"
print(file_name_check("e.txt"))  # 应该返回 "Yes"
print(file_name_check("ex.txt"))  # 应该返回 "Yes"
print(file_name_check("example.exe"))  # 应该返回 "Yes"
print(file_name_check("example.dll"))  # 应该返回 "Yes"
<jupyter_output>
Yes
No
Yes
No
No
No
No
No
Yes
Yes
Yes
Yes
<jupyter_text>
Problem 4: Sum of numbers in a string (10 points)Write a Python