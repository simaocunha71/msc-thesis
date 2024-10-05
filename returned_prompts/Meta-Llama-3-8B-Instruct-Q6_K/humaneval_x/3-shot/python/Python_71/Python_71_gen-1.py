    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return -1
    else:
        s = (sides[0] + sides[1] + sides[2]) / 2
        return round((s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5, 2)  # 0.5 for 2 decimal places


