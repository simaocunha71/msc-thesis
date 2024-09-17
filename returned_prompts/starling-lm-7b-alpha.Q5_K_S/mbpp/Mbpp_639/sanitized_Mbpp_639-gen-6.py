def sample_nam(list_name):
    sum_len = 0
    for name in list_name:
        if name[0].isupper():
            sum_len += len(name)
    return sum_len