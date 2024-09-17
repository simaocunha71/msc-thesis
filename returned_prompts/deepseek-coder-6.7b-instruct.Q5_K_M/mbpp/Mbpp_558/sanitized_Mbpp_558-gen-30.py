def digit_distance_nums(a,b):
    return sum(abs(int(x) - int(y)) for x, y in zip(str(a), str(b)))