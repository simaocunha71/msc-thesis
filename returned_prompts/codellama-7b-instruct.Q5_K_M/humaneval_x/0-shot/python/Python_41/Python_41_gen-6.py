

    # Base cases
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Recursive cases
    return n + car_race_collision(n - 1)

