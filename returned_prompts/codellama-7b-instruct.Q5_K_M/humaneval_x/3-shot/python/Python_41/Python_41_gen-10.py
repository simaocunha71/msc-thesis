    if n < 2:
        return 0

    # left to right cars
    l_to_r = [1] * n
    # right to left cars
    r_to_l = [1] * n

    # collision count
    collisions = 0

    # current position of left to right cars
    l_pos = 1
    # current position of right to left cars
    r_pos = 1

    # while both cars are moving
    while l_pos > 0 and r_pos > 0:
        l_pos += l_to_r[0]
        r_pos += r_to_l[0]
        if l_pos == r_pos:
            collisions += 1
            # remove first car from each set
            l_to_r.pop(0)
            r_to_l.pop(0)

    return collisions


