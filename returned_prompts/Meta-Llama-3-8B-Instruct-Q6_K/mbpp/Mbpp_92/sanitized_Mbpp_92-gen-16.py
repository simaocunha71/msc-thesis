def is_undulating(n):
    if len(str(n)) < 3:
        return False
    if str(n).endswith('1'):
        return True
    else:
        for i in range(len(str(n)) - 2):
            if str(n)[i] != '1':
                return False
        return True