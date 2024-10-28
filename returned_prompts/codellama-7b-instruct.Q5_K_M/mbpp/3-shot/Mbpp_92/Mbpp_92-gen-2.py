
def is_undulating(n):
    s = str(n)
    if len(s) == 1:
        return False
    diff = int(s[1:]) - int(s[:-1])
    return diff > 0


