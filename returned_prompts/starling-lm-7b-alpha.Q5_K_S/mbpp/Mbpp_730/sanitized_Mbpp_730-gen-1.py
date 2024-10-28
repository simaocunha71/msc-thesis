def consecutive_duplicates(list_):
    return [x for i, x in enumerate(list_, 1) if list_[i - 1] != x]