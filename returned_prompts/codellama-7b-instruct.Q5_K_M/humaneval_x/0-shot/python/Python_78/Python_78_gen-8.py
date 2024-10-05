
def hex_key(num):
    count = 0
    for i in num:
        if i in ['A', 'B', 'D', 'E', 'F']:
            count += 1
    return count
