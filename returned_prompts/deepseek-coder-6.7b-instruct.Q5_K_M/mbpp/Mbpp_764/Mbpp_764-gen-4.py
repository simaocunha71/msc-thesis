def number_ctr(s):
    ctr = 0
    for i in s:
        if i.isdigit():
            ctr += 1
    return ctr

print(number_ctr('program2bedone'))  # 1


