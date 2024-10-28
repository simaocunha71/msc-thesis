
def is_polite(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + 1
    else:
        return n + 2

def polite_number(n):
    i = 1
    num = 1
    while i <= n:
        num = is_polite(num)
        i += 1
    return num


