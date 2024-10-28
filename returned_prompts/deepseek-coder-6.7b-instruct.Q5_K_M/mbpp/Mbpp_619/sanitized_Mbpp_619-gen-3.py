def move_num(s):
    nums = [i for i in s if i.isdigit()]
    chars = [i for i in s if not i.isdigit()]
    return ''.join(chars) + ''.join(nums)