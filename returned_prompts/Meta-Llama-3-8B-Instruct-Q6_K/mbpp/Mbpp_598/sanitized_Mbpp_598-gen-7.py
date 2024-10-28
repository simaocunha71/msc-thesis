def armstrong_number(n):
    num = str(n)
    num_len = len(num)
    sum = 0
    for digit in num:
        sum += int(digit) ** num_len
    return sum == n