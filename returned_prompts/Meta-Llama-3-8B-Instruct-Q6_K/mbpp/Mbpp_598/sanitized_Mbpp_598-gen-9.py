def armstrong_number(n):
    num_str = str(n)
    n = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i)**n
    return sum == n