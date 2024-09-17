def merge(list_of_lists):
    result = [[], []]
    for sublist in list_of_lists:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result