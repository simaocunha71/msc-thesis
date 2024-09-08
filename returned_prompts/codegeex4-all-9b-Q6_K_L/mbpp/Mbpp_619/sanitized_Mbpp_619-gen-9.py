def move_num(s):
    nums = ''.join(filter(str.isdigit, s))
    letters = ''.join(filter(str.isalpha, s))
    return letters + nums