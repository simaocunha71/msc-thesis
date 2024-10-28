def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_val = 0
    for digit in num_str:
        sum_val += int(digit) ** num_len
    return sum_val == n