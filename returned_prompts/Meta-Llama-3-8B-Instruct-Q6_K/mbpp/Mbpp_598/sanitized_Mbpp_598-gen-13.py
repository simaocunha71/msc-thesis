def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** num_len
    return sum == n