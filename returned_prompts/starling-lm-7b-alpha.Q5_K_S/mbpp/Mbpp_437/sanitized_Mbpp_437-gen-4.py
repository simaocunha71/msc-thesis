def remove_odd(s):
    return "".join([c for c in s if ord(c) % 2 == 0])