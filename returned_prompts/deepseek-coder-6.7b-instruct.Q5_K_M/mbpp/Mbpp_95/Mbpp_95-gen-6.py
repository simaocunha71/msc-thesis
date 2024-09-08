def Find_Min_Length(lst):
    min_len = len(lst[0])
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
    return min_len

print(Find_Min_Length([[1],[1,2]])) # 1


