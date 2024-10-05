
def file_name_check(file_name):
    if len(file_name) > 3:
        return 'No'
    if not file_name.count('.') == 1:
        return 'No'
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    if not file_name.split('.')[1] in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'


