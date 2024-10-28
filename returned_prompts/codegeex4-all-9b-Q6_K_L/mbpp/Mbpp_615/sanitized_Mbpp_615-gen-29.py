def average_tuple(tup: tuple) -> list:
    avg_list = []
    for i in tup:
        avg_list.append(sum(i)/len(i))
    return avg_list