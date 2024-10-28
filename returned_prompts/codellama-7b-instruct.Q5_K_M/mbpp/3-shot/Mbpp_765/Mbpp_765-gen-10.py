
def is_polite(n):
    while True:
        n += 1
        if len(str(n)) == len(str(n)) + 1 and len(str(n)) == len(str(n)) - 1:
            return n


