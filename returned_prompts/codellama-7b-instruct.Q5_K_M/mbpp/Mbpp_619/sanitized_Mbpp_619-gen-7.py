def move_num(s):
    return ''.join([c for c in s if not c.isdigit()]) + ''.join(sorted(c for c in s if c.isdigit()))