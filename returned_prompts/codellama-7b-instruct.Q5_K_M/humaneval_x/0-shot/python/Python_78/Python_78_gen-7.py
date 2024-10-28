
def hex_key(num):
    num = str(num)
    count = 0
    for i in num:
        if i in '2357ABD':
            count += 1
    return count
