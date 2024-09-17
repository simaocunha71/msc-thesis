
def check_type(tup):
    data_type = type(tup[0])
    for i in tup:
        if type(i) != data_type:
            return False
    return True


