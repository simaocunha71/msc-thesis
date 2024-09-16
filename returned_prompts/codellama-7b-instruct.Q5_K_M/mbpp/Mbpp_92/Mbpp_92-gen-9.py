def is_undulating(num):
    if len(str(num)) <= 1:
        return False
    else:
        for i in range(len(str(num)) - 1):
            if int(str(num)[i]) > int(str(num)[i + 1]):
                return False
            if int(str(num)[i]) < int(str(num)[i + 1]):
                return True
    return False




