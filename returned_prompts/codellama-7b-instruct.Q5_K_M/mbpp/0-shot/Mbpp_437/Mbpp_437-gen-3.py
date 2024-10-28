def remove_odd(s):
    return ''.join([c for i, c in enumerate(s) if i % 2 == 0])
