def armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_val = 0
    for i in num_str:
        sum_val += int(i) ** num_len
    return sum_val == num