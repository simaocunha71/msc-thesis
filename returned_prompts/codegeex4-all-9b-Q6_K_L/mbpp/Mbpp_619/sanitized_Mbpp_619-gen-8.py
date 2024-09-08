def move_num(s):
    nums = [c for c in s if c.isdigit()]
    letters = [c for c in s if c.isalpha()]
    return ''.join(letters + nums)