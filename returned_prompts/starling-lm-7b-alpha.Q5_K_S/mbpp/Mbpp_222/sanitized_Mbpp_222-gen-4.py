def check_type(tup):
    tup_type = type(tup[0])
    for i in tup:
        if type(i) != tup_type:
            return False
    return True