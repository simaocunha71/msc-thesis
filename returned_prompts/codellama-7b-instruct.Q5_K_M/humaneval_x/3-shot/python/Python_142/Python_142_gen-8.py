    lst_cube = []
    lst_square = []

    for index, value in enumerate(lst):
        if index % 3 == 0:
            lst_cube.append(value ** 3)
        elif index % 4 == 0 and index % 3 != 0:
            lst_square.append(value ** 2)
        else:
            lst_cube.append(value)
            lst_square.append(value)

    return sum(lst_square) + sum(lst_cube)