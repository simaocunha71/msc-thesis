def pack_consecutive_duplicates(lst):
    result = []
    i = 0
    while i < len(lst):
        start = i
        while i < len(lst)-1 and lst[i] == lst[i+1]:
            i += 1
        result.append(lst[start:i+1])
        i += 1
    return result