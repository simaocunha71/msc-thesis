
def remove_odd(s):
    return ''.join(filter(lambda x: ord(x) % 2 == 0, s))


