
def move_num(s):
    nums = [i for i in s if i.isdigit()]
    letters = [i for i in s if i.isalpha()]
    return ''.join(letters + nums)

