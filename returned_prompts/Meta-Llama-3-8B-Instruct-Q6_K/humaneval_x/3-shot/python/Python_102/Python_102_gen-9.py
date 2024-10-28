    if x % 2 == 0:
        x_even = x
    else:
        x_even = x + 1

    if y % 2 == 0:
        y_even = y
    else:
        y_even = y - 1

    if x_even <= y_even:
        return x_even
    else:
        return -1


