def Split(x):
    new_list = []
    for i in x:
        if i % 2 != 0:
            new_list.append(i)
    return new_list