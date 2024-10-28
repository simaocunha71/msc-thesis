def armstrong_number(n):
    str_n = str(n)
    length = len(str_n)
    sum = 0
    for digit in str_n:
        sum += int(digit) ** length
    return sum == n