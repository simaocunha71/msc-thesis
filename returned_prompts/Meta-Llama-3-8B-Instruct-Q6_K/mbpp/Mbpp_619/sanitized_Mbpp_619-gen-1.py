def move_num(s):
    nums = ''
    result = ''
    for char in s:
        if char.isdigit():
            nums += char
        else:
            result += char
            if nums:
                result += nums
                nums = ''
    return result