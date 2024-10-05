    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('0123456789') > 3:
        return 'No'
    if file_name.startswith('.'):
        return 'No'
    if file_name.split('.')[0] == '':
        return 'No'
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
