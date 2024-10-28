    def check_name(name):
        if name.count(' ') != 0:
            return False
        if name.count('.') != 1:
            return False
        if name[0] in '0123456789':
            return False
        if name[-3::-1] != 'txt' and name[-3::-1] != 'dll' and name[-3::-1] != 'exe':
            return False
        if name[0] in '0123456789':
            return False
        return True

    if check_name(file_name):
        return 'Yes'
    else:
        return 'No'


