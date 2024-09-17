def remove_odd(s):
    res = ""
    for c in s:
        if int(c) % 2 == 0:
            res += c
    return res