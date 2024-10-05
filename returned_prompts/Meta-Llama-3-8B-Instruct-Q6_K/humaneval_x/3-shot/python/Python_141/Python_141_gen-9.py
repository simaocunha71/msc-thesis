    def is_valid(file_name):
        if len([char for char in file_name if char.isdigit()]) > 3:
            return False
        if file_name.count('.') != 1:
            return False
        if not file_name[:file_name.index('.')].isalnum():
            return False
        if file_name[file_name.index('.') + 1:].lower() not in ['txt', 'exe', 'dll']:
            return False
        return True

    if is_valid(file_name):
        return 'Yes'
    else:
        return 'No'
    # or
    return 'Yes' if is_valid(file_name) else 'No'  # one-liner
    # or
    result = is_valid(file_name)
    return 'Yes' if result else 'No'  # one-liner


