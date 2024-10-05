
def hex_key(num):
    count = 0
    if len(num) == 0:
        return count
    for i in range(len(num)):
        if num[i] in ['2', '3', '5', '7', 'B', 'D']:
            count += 1
    return count
