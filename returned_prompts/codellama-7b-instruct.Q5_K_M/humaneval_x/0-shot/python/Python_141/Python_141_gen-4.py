
def file_name_check(file_name):
    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif file_name.split('.')[0].strip() == '':
        return 'No'
    elif file_name.split('.')[1].strip() not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'


