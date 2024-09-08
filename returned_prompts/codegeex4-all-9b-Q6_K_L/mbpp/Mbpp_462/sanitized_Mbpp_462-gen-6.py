def combinations_list(lst):
    result = [[]]
    for i in range(len(lst)):
        for j in range(len(result)):
            result.append(result[j] + [lst[i]])
    return result