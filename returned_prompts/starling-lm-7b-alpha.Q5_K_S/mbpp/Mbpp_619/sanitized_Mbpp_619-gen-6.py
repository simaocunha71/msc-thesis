def move_num(s):
    numbers = []
    for c in s:
        if c.isdigit():
            numbers.append(c)
    for c in numbers:
        s = s.replace(c, '')
    return s + ''.join(numbers)