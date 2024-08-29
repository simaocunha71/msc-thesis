def move_num(s):
    chars = []
    nums = []
    for i in s:
        if i.isnumeric():
            nums.append(i)
        else:
            chars.append(i)
    return ''.join(chars + nums)