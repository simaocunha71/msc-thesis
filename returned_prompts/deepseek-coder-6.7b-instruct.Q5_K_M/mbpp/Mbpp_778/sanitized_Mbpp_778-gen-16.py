def pack_consecutive_duplicates(lst):
    res = []
    i = 0
    while i < len(lst):
        start = i
        while i + 1 < len(lst) and lst[i + 1] == lst[i]:
            i += 1
        res.append(lst[start:i+1])
        i += 1
    return res