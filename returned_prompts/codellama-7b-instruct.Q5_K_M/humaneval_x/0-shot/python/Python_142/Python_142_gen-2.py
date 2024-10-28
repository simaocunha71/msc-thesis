


def sum_squares(lst):
    new_list = []
    for i in range(len(lst)):
        if i%3 == 0:
            new_list.append(lst[i]**2)
        elif i%4 == 0 and i%3 != 0:
            new_list.append(lst[i]**3)
        else:
            new_list.append(lst[i])
    return sum(new_list)