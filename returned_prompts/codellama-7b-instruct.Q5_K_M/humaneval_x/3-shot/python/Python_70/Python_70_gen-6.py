    lst = sorted(lst)

    for i in range(len(lst)):
        if i % 2 == 0:
            yield lst[i]
        else:
            yield lst[-i - 1]
