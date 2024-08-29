def digit_distance_nums(a, b):
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    if len_a != len_b:
        return "Invalid numbers"
    sum_diff = 0
    for i in range(len_a):
        sum_diff += abs(int(str_a[i]) - int(str_b[i]))
    return sum_diff