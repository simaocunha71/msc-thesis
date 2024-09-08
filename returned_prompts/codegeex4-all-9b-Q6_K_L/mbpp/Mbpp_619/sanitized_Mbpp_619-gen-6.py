def move_num(s):
    nums = [c for c in s if c.isdigit()]
    letters = [c for c in s if not c.isdigit()]
    return ''.join(letters + nums)