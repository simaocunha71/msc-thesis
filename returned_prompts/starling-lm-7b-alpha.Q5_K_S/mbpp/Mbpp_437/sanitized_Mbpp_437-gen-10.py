def remove_odd(s):
    # your code
    return "".join(filter(lambda x: ord(x) % 2 == 0, s))