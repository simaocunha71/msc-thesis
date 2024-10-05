    if len(file_name) - file_name.count('.') > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    if not (file_name[0] in 'abcdefghijklmnopqrstuvwxyz' or file_name[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        return 'No'

    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


