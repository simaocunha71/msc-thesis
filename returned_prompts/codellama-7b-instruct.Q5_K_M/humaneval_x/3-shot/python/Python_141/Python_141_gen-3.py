    if len(file_name) > 3:
        return 'No'
    if file_name.count('.') > 1:
        return 'No'
    if file_name.count('.') == 0:
        return 'No'
    if file_name[0] not in range(97, 123) and file_name[0] not in range(65, 91):
        return 'No'
    if file_name.split('.')[1] != 'txt' and file_name.split('.')[1] != 'exe' and file_name.split('.')[1] != 'dll':
        return 'No'
    return 'Yes'


