def move_num(s):
    chars = []
    nums = []
    for char in s:
        if char.isnumeric():
            nums.append(char)
        else:
            chars.append(char)
    return ''.join(chars+nums)