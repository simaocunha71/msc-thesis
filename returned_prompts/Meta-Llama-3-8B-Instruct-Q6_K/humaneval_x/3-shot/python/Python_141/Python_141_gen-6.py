    import re
    if len(file_name) > 0:
        if len(re.findall(r'\d', file_name)) > 3:
            return 'No'
        if file_name.count('.') != 1:
            return 'No'
        if not re.match(r'^[a-zA-Z].*', file_name.split('.')[0]):
            return 'No'
        if file_name.split('.')[1].lower() not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'
    return 'No'  # file name is empty


