def substract_elements(t1, t2):
    return tuple(a - b for a, b in zip(t1, t2))

print(substract_elements((10, 4, 5), (2, 5, 18)))  # == (8, -1, -13)


