    if file_name.count('.') > 1:
        return 'No'
    if len(file_name.split('.')[0]) > 3:
        return 'No'
    if len(file_name.split('.')) > 2:
        if file_name.split('.')[1] not in ['exe', 'dll', 'txt']:
            return 'No'
    if file_name.split('.')[0][0].isalpha() == False:
        return 'No'
    return 'Yes'


