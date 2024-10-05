    import re

    # check if there is exactly one dot and name starts with a letter
    if file_name.count('.') != 1 or not file_name[0].isalpha():
        return 'No'

    # split the name into two parts before and after the dot
    name_parts = file_name.split('.')

    # check if name before the dot has more than three digits
    if len(re.findall(r'\d', name_parts[0])) > 3:
        return 'No'

    # check if name after the dot is one of the three allowed extensions
    if name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

