def merge(lists):
    results = [[], []]
    for sublist in lists:
        results[0].append(sublist[0])
        results[1].append(sublist[1])
    return results