def is_Diff(num):
    num_str = str(num)
    sum_odd = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
    sum_even = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
    return (sum_odd - sum_even) % 11 == 0