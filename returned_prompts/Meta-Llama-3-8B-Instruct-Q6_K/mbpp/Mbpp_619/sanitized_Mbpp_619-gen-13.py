def move_num(s):
    nums = []
    result = ''
    for char in s:
        if char.isdigit():
            nums.append(char)
        else:
            result += char
    return result + ''.join(nums)