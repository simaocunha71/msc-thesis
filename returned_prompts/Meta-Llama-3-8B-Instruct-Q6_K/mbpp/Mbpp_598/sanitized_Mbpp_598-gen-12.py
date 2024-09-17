def armstrong_number(n):
    num = str(n)
    sum = 0
    for i in num:
        sum += int(i) ** len(num)
    return sum == n