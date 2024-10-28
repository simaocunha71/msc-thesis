    squares = []
    cubes = []
    for i in range(len(lst)):
        if i % 3 == 0:
            squares.append(lst[i] ** 2)
        if i % 4 == 0 and i % 3 != 0:
            cubes.append(lst[i] ** 3)
    return sum(squares) + sum(cubes)


