def file_name_check(file_name):
    if file_name.count('.') > 1:
        return 'No'
    name, extension = file_name.split('.')
    if len(name) == 0 or not name[0].isalpha() or not name.isalnum() or not extension in ['txt', 'exe', 'dll']:
        return 'No'
    if sum(c.isdigit() for c in name) > 3:
        return 'No'
    return 'Yes'