    def is_valid_name(file_name):
        # Check if there are more than 3 digits
        digits = sum(c.isdigit() for c in file_name)
        if digits > 3:
            return False

        # Check if there is exactly one dot
        dot_count = file_name.count('.')
        if dot_count != 1:
            return False

        # Check if the name starts with a latin letter
        name_parts = file_name.split('.')
        if not name_parts[0].isalpha():
            return False

        # Check if the extension is valid
        valid_extensions = ['txt', 'exe', 'dll']
        if name_parts[1] not in valid_extensions:
            return False

        return True

    return 'Yes' if is_valid_name(file_name) else 'No'