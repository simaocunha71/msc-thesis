def merge(lists):
    result = [[], []]
    for l in lists:
        result[0].append(l[0])
        result[1].append(l[1])
    return result