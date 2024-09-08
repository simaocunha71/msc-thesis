def digit_distance_nums(a, b):
    a = str(a)
    b = str(b)
    sum = 0
    for i in range(min(len(a), len(b))):
        sum += abs(int(a[i]) - int(b[i]))
    return sum