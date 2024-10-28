    is_increasing = (l[0] < l[1]) and (l[1] < l[2]) and (l[2] < l[3])
    is_decreasing = (l[0] > l[1]) and (l[1] > l[2]) and (l[2] > l[3])
    return is_increasing or is_decreasing


