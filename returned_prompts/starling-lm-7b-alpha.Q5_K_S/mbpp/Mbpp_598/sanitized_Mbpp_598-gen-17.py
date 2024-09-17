def armstrong_number(n: int):
    s = str(n)
    length = len(s)
    total = 0
    for i in range(length):
        total += int(s[i]) ** length
    return total == n