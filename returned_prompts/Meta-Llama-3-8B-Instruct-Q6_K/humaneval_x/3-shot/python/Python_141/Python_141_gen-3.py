    def is_valid(file_name):
        if len(file_name) < 3:
            return False
        if file_name.count('.') != 1:
            return False
        before_dot, after_dot = file_name.rsplit('.', 1)
        if not before_dot[0].isalpha():
            return False
        if len([char for char in before_dot if char.isdigit()]) > 3:
            return False
        if after_dot not in ['txt', 'exe', 'dll']:
            return False
        return True

    return 'Yes' if is_valid(file_name) else 'No'  # Return 'Yes' if valid, 'No' otherwise


