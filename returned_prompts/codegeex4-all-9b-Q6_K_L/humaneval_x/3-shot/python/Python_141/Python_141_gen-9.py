    if len(file_name) > 3:
        return 'No'

    if file_name.count('.') != 1:
        return 'No'

    if file_name[0].isalpha() is False:
        return 'No'

    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

