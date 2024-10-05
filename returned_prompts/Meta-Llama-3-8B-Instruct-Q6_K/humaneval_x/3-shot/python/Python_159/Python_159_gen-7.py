    eaten = number
    remaining = remaining - number
    if remaining < need - number:
        eaten += need - remaining
        remaining = 0
    else:
        remaining -= need - number
    return [eaten + need, remaining]  # return the result as a list of two elements


