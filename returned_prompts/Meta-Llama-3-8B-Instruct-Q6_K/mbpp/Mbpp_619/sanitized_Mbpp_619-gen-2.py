def move_num(s):
    result = ''
    num = ''
    for char in s:
        if char.isdigit():
            num += char
        else:
            if num:
                result += num
                num = ''
            result += char
    if num:
        result += num
    return result