    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return -1
    s = (sides[0] + sides[1] + sides[2]) / 2
    area = (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5
    return round(area, 2)  # Round to 2 decimal points


