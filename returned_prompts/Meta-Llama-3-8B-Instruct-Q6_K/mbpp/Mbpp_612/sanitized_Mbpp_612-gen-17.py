def merge(list_of_lists):
    first, second = [], []
    for sublist in list_of_lists:
        first.append(sublist[0])
        second.append(sublist[1])
    return [first, second]