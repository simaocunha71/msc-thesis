def check_distinct(tup):
    return len(tup) == len(set(tup))  # set removes duplicates, if lengths are equal then there were no duplicates