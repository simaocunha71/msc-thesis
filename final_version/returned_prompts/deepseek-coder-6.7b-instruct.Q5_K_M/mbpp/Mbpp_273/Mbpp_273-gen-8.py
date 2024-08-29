def substract_elements(t1, t2):
    return tuple(i - j for i, j in zip(t1, t2))

print(substract_elements((10, 4, 5), (2, 5, 18)))


"""
