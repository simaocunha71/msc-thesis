def pack_consecutive_duplicates(lst):
    result = []
    sublist = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            sublist.append(lst[i])
        else:
            result.append(sublist)
            sublist = [lst[i]]
    result.append(sublist)
    return result