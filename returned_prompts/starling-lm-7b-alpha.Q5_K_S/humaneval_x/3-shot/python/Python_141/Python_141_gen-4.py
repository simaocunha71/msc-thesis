    def check(name):
        name = name.lower()
        if '.' not in name:
            return 'No'
        if name.count(' ') != 0:
            return 'No'
        if name[0] not in 'abcdefghijklmnopqrstuvwxyz' and name[0] != '.':
            return 'No'
        if name.count('.') != 1:
            return 'No'
        after_dot = name.split('.')[1]
        if after_dot not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'
    return check(file_name)


