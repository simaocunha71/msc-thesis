def frequency_lists(lists):
    flattened = [item for sublist in lists for item in sublist]
    return {x: flattened.count(x) for x in set(flattened)}