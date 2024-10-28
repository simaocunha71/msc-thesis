def pack_consecutive_duplicates(lst):
    result = []
    current_sublist = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_sublist.append(lst[i])
        else:
            result.append(current_sublist)
            current_sublist = [lst[i]]
    result.append(current_sublist)
    return result