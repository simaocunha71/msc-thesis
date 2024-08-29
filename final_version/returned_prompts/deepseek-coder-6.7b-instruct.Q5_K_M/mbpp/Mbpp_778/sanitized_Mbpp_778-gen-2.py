def pack_consecutive_duplicates(lst):
    result = []
    temp = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            temp.append(lst[i])
        else:
            result.append(temp)
            temp = [lst[i]]
    result.append(temp)
    return result