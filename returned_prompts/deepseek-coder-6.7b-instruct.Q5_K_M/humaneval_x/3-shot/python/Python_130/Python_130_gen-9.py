    if n == 0:
        return [0]
    elif n == 1:
        return [0, 3]
    elif n == 2:
        return [0, 3, 2]

    tri_list = [0, 3, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tri_list.append(2)
        else:
            tri_list.append(tri_list[-1] + tri_list[-2] + tri_list[-3])

    return tri_list


