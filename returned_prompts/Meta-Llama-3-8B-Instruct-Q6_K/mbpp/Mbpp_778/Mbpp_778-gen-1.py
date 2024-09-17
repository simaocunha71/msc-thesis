def pack_consecutive_duplicates(lst):
    result = []
    current_group = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_group.append(lst[i])
        else:
            result.append(current_group)
            current_group = [lst[i]]
    result.append(current_group)
    return result
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))



# 2
