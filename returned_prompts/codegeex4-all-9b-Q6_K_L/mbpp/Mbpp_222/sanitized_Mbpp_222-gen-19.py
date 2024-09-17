def check_type(tup):
    type_ = type(tup[0])
    for i in tup:
        if type(i) != type_:
            return False
    return True