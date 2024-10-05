
def hex_key(num):
    if num == '':
        return 0
    count = 0
    for i in num:
        if i == '2' or i == '3' or i == '5' or i == '7' or i == 'B' or i == 'D':
            count += 1
    return count

