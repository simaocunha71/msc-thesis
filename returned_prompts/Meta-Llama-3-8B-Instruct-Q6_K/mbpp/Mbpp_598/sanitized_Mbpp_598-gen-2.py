def armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
    return sum == n