def digit_distance_nums(a, b):
    a = str(a)
    b = str(b)
    sum = 0
    for i in range(0, len(a)):
        sum += abs(int(a[i]) - int(b[i]))
    return sum