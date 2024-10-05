    import re
    # Check the first condition
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    # Check the second condition
    if file_name.count('.') != 1:
        return 'No'
    # Check the third condition
    if not file_name[0].isalpha():
        return 'No'
    # Check the fourth condition
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    # If all conditions are met
    return 'Yes'


