def digit_distance_nums(a, b):
    a_str = str(a)
    b_str = str(b)
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    total = 0
    for i in range(max_len):
        digit_a = int(a_str[i])
        digit_b = int(b_str[i])
        total += abs(digit_a - digit_b)
    return total