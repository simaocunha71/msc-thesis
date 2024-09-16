def move_num(s):
    nums = list(filter(str.isdigit, s))
    return ''.join(filter(str.isalpha, s)) + ''.join(nums)

# 2018-09-23 1.34.37(+0000)
# 2018-09-23 1.35.06(+0000)
