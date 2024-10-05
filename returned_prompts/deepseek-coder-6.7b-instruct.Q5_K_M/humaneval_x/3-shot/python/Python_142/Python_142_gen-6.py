    sum_val = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            sum_val += val ** 2
        elif idx % 4 == 0:
            sum_val += val ** 3
    return sum_val


