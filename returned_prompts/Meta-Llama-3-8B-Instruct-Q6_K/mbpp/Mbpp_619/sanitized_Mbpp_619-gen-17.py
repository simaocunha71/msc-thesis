def move_num(s):
    nums = '0123456789'
    str_nums = ''
    result = ''
    for char in s:
        if char in nums:
            str_nums += char
        else:
            result += char
    result += str_nums
    return result