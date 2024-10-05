    def is_valid(name):
        if len(name) > 3:
            return False
        if not name.isalnum():
            return False
        if not name[0].isalpha():
            return False
        return True

    if '.' not in file_name:
        return 'No'

    name, extension = file_name.split('.')
    if not is_valid(name):
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

