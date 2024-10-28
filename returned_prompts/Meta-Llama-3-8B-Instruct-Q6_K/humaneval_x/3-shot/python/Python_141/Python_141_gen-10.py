    def is_valid(name):
        parts = name.split('.')
        if len(parts) != 2:
            return False
        if not parts[0][0].isalpha():
            return False
        if len(parts[0]) > 1 and not parts[0][1:].isdigit():
            return False
        if len(parts[1]) > 3:
            return False
        if parts[1] not in ['txt', 'exe', 'dll']:
            return False
        return True

    return 'Yes' if is_valid(file_name) else 'No'  # replace this with your desired return statement.