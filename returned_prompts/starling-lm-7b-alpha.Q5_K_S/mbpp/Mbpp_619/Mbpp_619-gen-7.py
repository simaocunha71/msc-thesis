
def move_num(s):
    nums = [i for i in s if i.isdigit()]
    s = s.replace(str(nums), '')
    return s + ''.join(nums)


