
def file_name_check(file_name):
    if file_name.count('.') != 1 or file_name.count('0')+file_name.count('1')+file_name.count('2')+file_name.count('3')+file_name.count('4')+file_name.count('5')+file_name.count('6')+file_name.count('7')+file_name.count('8')+file_name.count('9') > 3:
        return 'No'
    name, extension = file_name.split('.')
    if not name or not name[0].isalpha() or not extension in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'  (the name should start with a latin alphapet letter)
print(file_name_check("ex.ample.txt"))  # => 'No'  (more than one dot)
print(file_name_check("example.exe"))  # => 'Yes'
print(file_name_check("exam123ple.dll"))  # => 'No'  (more than three digits)

"""
This solution works by first checking if the file name follows the given conditions,
that is, if it contains exactly one dot and no more than three digits. If it doesn't,
it returns 'No'. Then it splits the file name into two parts: the name before the dot,
and the name after the dot. If the name before the dot is empty, or if the name does not
start with a letter, or if the extension is not one of the specified ones, it returns 'No'.
Otherwise, it returns 'Yes'.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2 Given a string, return a string where for every char in the original, there are two chars.Examples```double_char("String") ➞ "SSttrriinngg"double_