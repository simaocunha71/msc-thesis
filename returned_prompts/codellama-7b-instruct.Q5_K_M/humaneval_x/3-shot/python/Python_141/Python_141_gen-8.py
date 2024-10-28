    if len(file_name) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif file_name.split('.')[0] == '':
        return 'No'
    elif file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'


