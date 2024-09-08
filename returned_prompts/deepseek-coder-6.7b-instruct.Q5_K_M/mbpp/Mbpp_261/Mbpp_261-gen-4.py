def division_elements(t1, t2):
    return tuple(x // y for x, y in zip(t1, t2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))

Explanation:
In the function, we use the zip() function to iterate over the elements of both tuples simultaneously. For each pair of elements (x, y), we perform an integer division operation (//). The result is a new tuple which we then return.

"""
