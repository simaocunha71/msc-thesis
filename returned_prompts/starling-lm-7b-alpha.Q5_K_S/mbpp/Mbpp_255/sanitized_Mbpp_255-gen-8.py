from itertools import chain, combinations
def combinations_colors(list, length):
    result = []
    for i in range(len(list)):
        result.append(tuple(list[i] for _ in range(length)))
    return result