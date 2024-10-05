    third_elements = sorted(l[i] for i in range(0, len(l), 3))
    for i in range(0, len(l), 3):
        l[i] = third_elements.pop(0)

    return l

