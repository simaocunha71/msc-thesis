def pack_consecutive_duplicates(lst):
    if not lst:
        return []

    packed = [[lst[0]]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            packed[-1].append(lst[i])
        else:
            packed.append([lst[i]])

    return packed