
def get_row(lst, x):
    coords = [(i, index) for i, row in enumerate(lst) for index in range(len(row)) if x == row[index]]
    coords.sort(key=lambda x: x[0])
    for i in range(len(coords)):
        coords[i] = (coords[i][0], sorted(coords[i][1:], key=lambda x: x, reverse=True))
    return coords

#test
get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1)

#test
get_row([], 1)

#test
get_row([[], [1], [1, 2, 3]], 3)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 2)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 3)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 4)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 5)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 6)

#test
get_row([
    [1,2,3],
    [1,2,3,4],
    [1,2]
], 7)

#test
get_row([
    [],
    [],
    []
], 1)

#test
get_row([[], [], [1]], 1)

#test
get_row([[], [], [