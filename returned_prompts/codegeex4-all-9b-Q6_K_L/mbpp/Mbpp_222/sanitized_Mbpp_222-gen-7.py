def check_type(tup):
    if len(tup) == 0:
        return True
    first_type = type(tup[0])
    for i in tup:
        if type(i) != first_type:
            return False
    return True