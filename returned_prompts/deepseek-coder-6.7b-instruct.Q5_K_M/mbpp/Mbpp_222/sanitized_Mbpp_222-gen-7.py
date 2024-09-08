def check_type(tup):
    type_check = type(tup[0])
    for i in tup[1:]:
        if type(i) != type_check:
            return False
    return True