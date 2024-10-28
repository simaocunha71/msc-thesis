    eaten = number + need
    left = remaining - eaten

    if left < 0:
        left = 0

    return [eaten, left]


