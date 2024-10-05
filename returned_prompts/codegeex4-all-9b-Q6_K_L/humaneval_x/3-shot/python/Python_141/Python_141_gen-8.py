    import re

    def is_valid(file_name):
        # Check for more than three digits
        if sum(c.isdigit() for c in file_name) > 3:
            return False

        # Check for exactly one dot
        if file_name.count('.') != 1:
            return False

        # Check for valid name before dot
        name_before_dot = file_name.split('.')[0]
        if not re.match(r'^[a-zA-Z]', name_before_dot):
            return False

        # Check for valid extension
        extension = file_name.split('.')[-1]
        if extension not in ['txt', 'exe', 'dll']:
            return False

        return True

    return 'Yes' if is_valid(file_name) else 'No'

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))

