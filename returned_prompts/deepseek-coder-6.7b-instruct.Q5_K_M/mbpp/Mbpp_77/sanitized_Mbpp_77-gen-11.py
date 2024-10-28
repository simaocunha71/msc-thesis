def is_Diff(num):
    num_str = str(num)
    sum_diff = sum(int(num_str[i]) - int(num_str[i+1]) for i in range(len(num_str)-1))
    return abs(sum_diff) % 11 == 0