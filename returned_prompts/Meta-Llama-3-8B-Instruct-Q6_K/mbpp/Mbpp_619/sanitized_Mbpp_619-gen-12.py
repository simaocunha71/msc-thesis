def move_num(s):
    nums = ''
    result = ''
    for char in s:
        if char.isdigit():
            nums += char
        else:
            result += char
    return result + nums