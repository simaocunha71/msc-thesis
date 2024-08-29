def division_elements(t1, t2):
    return tuple(x // y for x, y in zip(t1, t2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))


"""
