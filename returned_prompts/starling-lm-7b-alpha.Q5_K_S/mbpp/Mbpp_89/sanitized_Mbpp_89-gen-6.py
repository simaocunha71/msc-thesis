def closest_num(n):
    # get the nearest number
    nearest_num = n
    while True:
        if nearest_num > 0 and nearest_num % 2 == 0:
            break
        nearest_num -= 1
    return nearest_num