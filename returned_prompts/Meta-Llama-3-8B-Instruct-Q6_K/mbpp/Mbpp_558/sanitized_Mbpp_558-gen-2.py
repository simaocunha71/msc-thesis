def digit_distance_nums(a, b):
    return sum(abs(int(i) - int(j)) for i, j in zip(str(a), str(b))) if len(str(a)) == len(str(b)) else None