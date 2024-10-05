    eaten = number
    carrots_left = remaining

    if need > remaining:
        eaten += remaining
        carrots_left = 0
    else:
        eaten += need
        carrots_left -= need

    return [eaten, carrots_left]


