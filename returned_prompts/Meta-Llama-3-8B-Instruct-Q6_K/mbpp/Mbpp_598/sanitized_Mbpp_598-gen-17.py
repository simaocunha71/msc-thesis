def armstrong_number(n):
    num = str(n)
    length = len(num)
    sum = 0
    for digit in num:
        sum += int(digit) ** length
    return sum == n