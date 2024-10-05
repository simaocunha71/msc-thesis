    for i in range(len(lst)):
        if lst[i] >= 1:
            if lst[i] > 1 and lst.count(lst[i]) >= lst[i]:
                return lst[i]
            elif lst[i] == 1 and lst.count(lst[i]) > 1:
                return lst[i]
        else:
            continue

    return -1


