def combinations_list(lst: list) -> list:
    result = [[]]
    for i in range(len(lst)):
        for j in range(len(result)):
            new_combination = result[j] + [lst[i]]
            result.append(new_combination)
    return result