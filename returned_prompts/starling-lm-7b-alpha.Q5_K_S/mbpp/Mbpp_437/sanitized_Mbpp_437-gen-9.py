def remove_odd(s):
    res = ""
    for c in s:
        if ord(c) % 2 == 0:
            res += c
    return res