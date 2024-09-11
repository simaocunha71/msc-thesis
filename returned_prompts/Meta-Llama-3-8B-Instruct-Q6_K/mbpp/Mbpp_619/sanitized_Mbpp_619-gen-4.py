def move_num(s):
    letters = [c for c in s if not c.isdigit()]
    nums = [c for c in s if c.isdigit()]
    return ''.join(letters + nums)  # Join the letters and numbers back together. 