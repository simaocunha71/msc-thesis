def dict_depth(d):
    if type(d) == type({}) or type(d) == type([]):
        return 1 + max(map(dict_depth, d.values()))
    else:
        return 0