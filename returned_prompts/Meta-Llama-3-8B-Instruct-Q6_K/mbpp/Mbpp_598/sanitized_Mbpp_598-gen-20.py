def armstrong_number(n):
    num = str(n)
    if len(num) > 3:
        return False
    sum = 0
    for i in num:
        sum += int(i) ** len(num)
    return sum == n