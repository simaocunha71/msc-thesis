def sum_list(a, b):
    max_len = max(len(a), len(b))
    a += [0] * (max_len - len(a))
    b += [0] * (max_len - len(b))
    return [x+y for x,y in zip(a,b)]