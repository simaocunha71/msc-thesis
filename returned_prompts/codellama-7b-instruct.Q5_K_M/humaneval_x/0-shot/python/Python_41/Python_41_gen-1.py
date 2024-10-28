
    if n == 1:
        return 0
    if n == 2:
        return 1

    left_cars = range(1, n + 1)
    right_cars = range(n, 0, -1)

    num_collisions = 0
    for left in left_cars:
        for right in right_cars:
            if left + right == n + 1:
                num_collisions += 1

    return num_collisions


