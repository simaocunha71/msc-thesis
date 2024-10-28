def move_num(s):
    numbers = ''
    rest = ''
    for char in s:
        if char.isdigit():
            numbers += char
        else:
            rest += char
    return rest + numbers