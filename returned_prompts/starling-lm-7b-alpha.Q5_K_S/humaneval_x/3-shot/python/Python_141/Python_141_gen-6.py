    if len(file_name) <= 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    if not file_name[0].isalpha():
        return 'No'
    if file_name.endswith('.txt') or file_name.endswith('.exe') or file_name.endswith('.dll'):
        return 'Yes'
    else:
        return 'No'


