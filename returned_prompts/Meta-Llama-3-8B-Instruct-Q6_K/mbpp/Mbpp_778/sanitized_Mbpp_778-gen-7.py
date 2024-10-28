def pack_consecutive_duplicates(lst):
    result = [[x] for x in set(lst)]
    for x in lst:
        for i, sublist in enumerate(result):
            if sublist[0] == x:
                if len(sublist) == 1 or sublist[-1] != x:
                    result[i].append(x)
                break
    return result