def count_X(tup, elm):
    return tup.count(elm)

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # should return 0

# Alternate solution
def count_X(tup, elm):
    count = 0
    for i in tup:
        if i == elm:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # should return 0

# Third solution
def count_X(tup, elm):
    return len([i for i in tup if i == elm])

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4)) # should return 0

