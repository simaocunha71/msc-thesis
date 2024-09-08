
def check_distinct(tup):
    return len(tup) == len(set(tup))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False


