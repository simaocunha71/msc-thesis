def file_name_check(file_name):
    # Check if there are more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    # Split the file name into the name and extension
    name, extension = file_name.split('.')
    # Check if the name starts with a latin alphapet letter
    if not name[0].isalpha():
        return 'No'
    # Check if the extension is one of the allowed extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'