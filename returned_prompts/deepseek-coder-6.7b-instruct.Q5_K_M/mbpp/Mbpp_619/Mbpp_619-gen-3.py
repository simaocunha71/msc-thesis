def move_num(s):
    nums = [i for i in s if i.isdigit()]
    chars = [i for i in s if not i.isdigit()]
    return ''.join(chars) + ''.join(nums)

print(move_num('I1love143you55three3000thousand'))  # Iloveyouthreethousand1143553000


"""
