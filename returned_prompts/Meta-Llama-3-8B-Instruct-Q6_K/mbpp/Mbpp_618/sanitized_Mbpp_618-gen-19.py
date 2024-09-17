def div_list(list1, list2):
    result = []
    for i, j in zip(list1, list2):
        try:
            result.append(i/j)
        except ZeroDivisionError:
            result.append(0)
    return result