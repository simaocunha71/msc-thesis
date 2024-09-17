def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        sum += int(num_str[i])**num_len
    return sum == n