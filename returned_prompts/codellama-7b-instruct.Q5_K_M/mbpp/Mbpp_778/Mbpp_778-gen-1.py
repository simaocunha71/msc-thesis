"""
def pack_consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append([lst[i]])
        else:
            if lst[i] != lst[i-1]:
                result.append([lst[i]])
            else:
                result[-1].append(lst[i])
    return result
"""
