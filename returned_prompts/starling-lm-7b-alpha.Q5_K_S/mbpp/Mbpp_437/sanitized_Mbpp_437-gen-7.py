def remove_odd(s):
    ret = ""
    for c in s:
        if ord(c) % 2 == 0:
            ret += c
    return ret