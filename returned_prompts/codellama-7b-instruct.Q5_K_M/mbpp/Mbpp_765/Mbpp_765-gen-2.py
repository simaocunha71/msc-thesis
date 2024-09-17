
def is_polite(n):
    if n < 10:
        return n
    s = str(n)
    count = 0
    for i in s:
        if int(i) > 0 and int(i) % 2 == 0:
            count += 1
    if count > 1:
        return n + 14
    else:
        return n + 6


