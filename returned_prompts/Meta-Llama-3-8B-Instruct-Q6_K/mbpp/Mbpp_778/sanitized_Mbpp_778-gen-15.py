def pack_consecutive_duplicates(lst):
    result = []
    temp = []
    for i in lst:
        if not temp or i != temp[-1]:
            if temp:
                result.append(temp)
            temp = [i]
        else:
            temp.append(i)
    if temp:
        result.append(temp)
    return result