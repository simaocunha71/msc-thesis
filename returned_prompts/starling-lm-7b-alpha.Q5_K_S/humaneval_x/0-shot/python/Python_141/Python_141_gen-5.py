
def file_name_check(file_name):
    import re
    digits_count = len(re.findall(r'\d', file_name))
    if digits_count > 3 or len(re.findall(r'\.', file_name)) != 1:
        return 'No'
    else:
        if file_name[0] in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' and file_name[-3:] in ['txt', 'exe', 'dll']:
            return 'Yes'
        else:
            return 'No'

print(file_name_check("1example.dll"))
print(file_name_check("example.txt"))




# Another Solution
def file_name_check(file_name):
    if len(re.findall(r'\d', file_name)) > 3 or len(re.findall(r'\.', file_name)) != 1:
        return 'No'
    if not file_name[0].isalpha():
        return 'No'
    if not (file_name[-3:] in ['txt', 'exe', 'dll']):
        return 'No'
    return 'Yes'




# Another Solution
def file_name_check(file_name):
    return (len(re.findall(r'\d', file_name)) <= 3) and (len(re.findall(r'\.', file_name)) == 1) and (file_name[0].isalpha()) and (file_name[-3:] in ['txt', 'exe', 'dll'])




# Another Solution
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    if not file_name[0].isalpha():
        return 'No'
    if len(re.findall(r'\d', file_name)) > 3:
        return '