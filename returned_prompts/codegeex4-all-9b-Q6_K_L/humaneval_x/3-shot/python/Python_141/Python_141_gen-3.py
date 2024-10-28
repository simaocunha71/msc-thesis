    if not file_name:
        return 'No'

    if not file_name.count('.') == 1:
        return 'No'

    if not file_name[0].isalpha():
        return 'No'

    if not file_name.split('.')[-1] in ['txt', 'exe', 'dll']:
        return 'No'

    if len([c for c in file_name if c.isdigit()]) > 3:
        return 'No'

    return 'Yes'