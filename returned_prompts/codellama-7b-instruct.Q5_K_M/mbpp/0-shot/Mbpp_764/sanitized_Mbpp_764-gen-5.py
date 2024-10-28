def number_ctr(strg):
    num_ctr = 0
    for char in strg:
        if char.isdigit():
            num_ctr += 1
    return num_ctr