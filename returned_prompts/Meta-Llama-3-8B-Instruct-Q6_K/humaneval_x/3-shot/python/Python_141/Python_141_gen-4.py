    def is_valid(file_name):
        parts = file_name.split('.')
        if len(parts) != 2:
            return False
        if not parts[0][0].isalpha():
            return False
        if not parts[1] in ['txt', 'exe', 'dll']:
            return False
        if sum(c.isdigit() for c in file_name) > 3:
            return False
        return True

    return 'Yes' if is_valid(file_name) else 'No'
