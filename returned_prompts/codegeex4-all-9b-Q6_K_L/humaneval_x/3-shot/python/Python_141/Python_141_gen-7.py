    if not file_name.count('.') == 1:
        return 'No'

    if not file_name[0].isalpha():
        return 'No'

    if not file_name[file_name.index('.') + 1:].lower() in ['txt', 'exe', 'dll']:
        return 'No'

    if not file_name.count('0123456789') <= 3:
        return 'No'

    return 'Yes'