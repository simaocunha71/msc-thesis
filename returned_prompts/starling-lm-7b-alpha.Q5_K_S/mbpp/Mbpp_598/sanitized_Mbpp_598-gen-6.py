def armstrong_number(n):
    n = str(n)
    length = len(n)
    total = 0
    for i in n:
        total += int(i) ** length
    return total == int(n)