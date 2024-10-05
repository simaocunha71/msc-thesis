    # convert the given number to float
    num = float(value)

    # check if the number is a positive integer
    if num.is_integer():
        return int(num)

    # if not, find the closest integer
    if num > 0:
        return int(num) + (int(num) % 1 != 0)
    else:
        return int(num) - (int(num) % 1 != 0)


