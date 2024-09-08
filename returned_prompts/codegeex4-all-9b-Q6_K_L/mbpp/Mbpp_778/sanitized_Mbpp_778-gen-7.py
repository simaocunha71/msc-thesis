def pack_consecutive_duplicates(lst):
    result = []
    temp = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            if temp:
                result.append(temp)
                temp = []
            temp.append(lst[i])
        else:
            temp.append(lst[i])
    if temp:
        result.append(temp)
    return result