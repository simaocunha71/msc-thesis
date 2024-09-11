def median_trapezium(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        return (sides[0] + sides[1]) / 2
    else:
        return (sides[1] + sides[2]) / 2