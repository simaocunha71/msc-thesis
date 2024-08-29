def substract_elements(tuple1, tuple2):
    return tuple(i - j for i, j in zip(tuple1, tuple2))

print(substract_elements((10, 4, 5), (2, 5, 18)))

# Output:
# (8, -1, -13)


