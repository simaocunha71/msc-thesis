def move_num(s):
    nums = ''
    letters = ''
    for i in s:
        if i.isnumeric():
            nums += i
        else:
            letters += i
    return letters+nums