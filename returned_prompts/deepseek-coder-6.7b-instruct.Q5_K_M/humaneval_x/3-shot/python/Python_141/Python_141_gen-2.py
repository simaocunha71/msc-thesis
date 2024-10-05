    import re

    # Check if there are more than 3 digits in the file's name.
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'

    # Check if there is exactly one dot in the file's name.
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is not empty and starts with a letter.
    if not re.match(r'[a-zA-Z].*', file_name.split('.')[0]):
        return 'No'

    # Check if the substring after the dot is one of ['txt', 'exe', 'dll'].
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


