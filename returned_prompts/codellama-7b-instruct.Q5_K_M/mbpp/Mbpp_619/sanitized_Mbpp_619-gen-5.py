def move_num(s):
    nums = list(filter(str.isdigit, s))
    return ''.join(filter(str.isalpha, s)) + ''.join(nums)