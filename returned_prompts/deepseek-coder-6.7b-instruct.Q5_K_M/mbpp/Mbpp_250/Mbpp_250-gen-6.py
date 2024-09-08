def count_X(tup, elem):
    count = 0
    for i in tup:
        if i == elem:
            count += 1
    return count

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4))

# The output will be 0 as there is no element 4 in the tuple.

