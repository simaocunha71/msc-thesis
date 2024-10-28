def move_num(s):
    numbers = ''.join([c for c in s if c.isdigit()])
    letters = ''.join([c for c in s if not c.isdigit()])
    return letters + numbers