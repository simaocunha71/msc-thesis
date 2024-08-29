def check_type(tup):
    type_check = type(tup[0])
    for i in range(1, len(tup)):
        if type(tup[i]) != type_check:
            return False
    return True