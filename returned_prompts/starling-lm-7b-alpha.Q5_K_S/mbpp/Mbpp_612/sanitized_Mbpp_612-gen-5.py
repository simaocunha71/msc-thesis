def merge(lst):
    first, second = [], []
    for sublist in lst:
        first.append(sublist[0])
        second.append(sublist[1])
    return [first, second]