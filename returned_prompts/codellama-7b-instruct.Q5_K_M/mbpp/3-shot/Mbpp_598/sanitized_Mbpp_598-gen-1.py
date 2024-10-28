def armstrong_number(n):
    n = str(n)
    total = 0
    for i in n:
        total += int(i) ** 3
    if total == n:
        return True
    else:
        return False