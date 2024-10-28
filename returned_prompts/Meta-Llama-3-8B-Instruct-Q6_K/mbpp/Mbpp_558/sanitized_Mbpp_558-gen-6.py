def digit_distance_nums(m, n):
    return sum(abs(int(x) - int(y)) for x, y in zip(str(m), str(n)))  # Python 3.5+