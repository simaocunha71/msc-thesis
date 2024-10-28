def move_num(s):
    nums = ''.join(c for c in s if c.isdigit())
    letters = ''.join(c for c in s if c.isalpha())
    return letters + nums