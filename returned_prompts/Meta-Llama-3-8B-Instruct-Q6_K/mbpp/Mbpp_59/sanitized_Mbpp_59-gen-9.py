def is_octagonal(n):
    if n < 1:
        return None
    return int((8*n**3 - 13*n**2 + 8*n) / 2)  # calculate the nth octagonal number
    # return int((3 - math.sqrt(1 + 16*n)) / 2)  # calculate the nth octagonal number
    # return int((3 + math.sqrt(1 + 16*n)) / 2)  # calculate the nth octagonal number