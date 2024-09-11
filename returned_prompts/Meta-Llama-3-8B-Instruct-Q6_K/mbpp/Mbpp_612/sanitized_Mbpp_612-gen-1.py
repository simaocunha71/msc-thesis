def merge(lists):
    result = [[], []]
    for sublist in lists:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return [result[0], result[1]]