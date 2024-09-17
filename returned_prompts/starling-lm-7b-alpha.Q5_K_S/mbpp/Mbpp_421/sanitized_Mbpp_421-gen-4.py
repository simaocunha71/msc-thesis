def concatenate_tuple(t):
    t_str = ''
    for i in t:
        t_str += str(i) + '-'
    return t_str[:-1]