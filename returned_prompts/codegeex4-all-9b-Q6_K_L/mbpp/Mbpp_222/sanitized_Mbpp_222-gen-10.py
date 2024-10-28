def check_type(tup):
    if len(tup) == 0:
        return True
    else:
        return all(type(tup[0]) == type(x) for x in tup)