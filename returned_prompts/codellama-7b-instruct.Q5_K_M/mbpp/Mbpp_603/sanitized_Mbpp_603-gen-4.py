def get_ludic(max):
    ludics = [2, 3, 5, 7]
    for i in range(11, max + 1):
        for j in ludics:
            if i % j == 0:
                break
        else:
            ludics.append(i)
    return ludics