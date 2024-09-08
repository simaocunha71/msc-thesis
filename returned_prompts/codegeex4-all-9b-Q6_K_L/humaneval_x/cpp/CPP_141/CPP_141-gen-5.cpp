def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    elif not file_name[:file_name.find('.')].isalpha():
        return 'No'
    elif file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
        return 'No'
    elif file_name[file_name.find('.'):] not in ['.txt', '.exe', '.dll']:
        return 'No'
    else:
        return 'Yes'

print(file_name_check('example.txt'))
print(file_name_check('1example.dll'))
print(file_name_check('example'))
print(file_name_check('example.'))
print(file_name_check('exa1234mple.txt'))
print(file_name_check('example.exe'))



