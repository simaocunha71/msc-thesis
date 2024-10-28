def recursive_list_sum(l):
    if isinstance(l, list):
        return sum(map(recursive_list_sum, l))
    else:
        return l