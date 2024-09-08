def move_num(s):
    letters = [c for c in s if not c.isdigit()]
    numbers = [c for c in s if c.isdigit()]
    return ''.join(letters + numbers)