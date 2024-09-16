def is_polite(n):
    if n == 1:
        return n
    while True:
        n += 1
        if is_polite_number(n):
            return n
def is_polite_number(n):
    return all(d*2 <= n for d in str(n))