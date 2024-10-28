    total_eaten = number
    total_carrots = number
    while total_carrots < need and remaining > 0:
        total_eaten += 1
        total_carrots += 1
        remaining -= 1
    return [total_eaten, remaining]


