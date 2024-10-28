
def digit_distance_nums(a,b):
    a, b = str(a), str(b)
    return sum(abs(int(x) - int(y)) for x, y in zip(a, b))


