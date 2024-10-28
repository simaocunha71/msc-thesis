    def is_valid_file_name(file_name):
        if file_name.count('.') != 1:
            return 'No'
        before_dot, after_dot = file_name.rsplit('.', 1)
        if not before_dot[0].isalpha() or len(before_dot) > 0:
            return 'No'
        if len([c for c in before_dot if c.isdigit()]) > 3:
            return 'No'
        if after_dot not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'

    return is_valid_file_name(file_name)
