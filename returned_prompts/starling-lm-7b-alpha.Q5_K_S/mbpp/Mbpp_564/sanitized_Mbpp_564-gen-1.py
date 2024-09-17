def count_Pairs(list_int, n):
    count = 0
    for i in range(len(list_int)):
        for j in range(i + 1, len(list_int)):
            if list_int[i] != list_int[j]:
                count += 1
    return count