def is_undulating(n):
    s = str(n)
    return s != ''.join(map(str, [int(i) for i in s]))