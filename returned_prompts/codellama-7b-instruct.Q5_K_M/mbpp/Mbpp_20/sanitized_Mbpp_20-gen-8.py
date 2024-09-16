def is_woodall(num):
    s = str(num)
    return s == ''.join(sorted(s))