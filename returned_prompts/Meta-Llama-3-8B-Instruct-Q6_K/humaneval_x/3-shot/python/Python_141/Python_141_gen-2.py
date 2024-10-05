    def is_valid(file_name):
        if not isinstance(file_name, str):
            return 'No'
        if len(file_name) == 0:
            return 'No'
        if len(file_name.split('.')) != 2:
            return 'No'
        before_dot, after_dot = file_name.split('.')
        if not before_dot[0].isalpha():
            return 'No'
        if len([c for c in before_dot if c.isdigit()]) > 3:
            return 'No'
        if after_dot not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'

    return is_valid(file_name)  # returns 'Yes' or 'No' based on the conditions


