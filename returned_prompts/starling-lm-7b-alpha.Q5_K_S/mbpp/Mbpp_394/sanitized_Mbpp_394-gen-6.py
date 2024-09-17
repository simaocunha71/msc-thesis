def check_distinct(tup):
    tup_set = {x for x in tup}
    return len(tup_set) == len(tup)