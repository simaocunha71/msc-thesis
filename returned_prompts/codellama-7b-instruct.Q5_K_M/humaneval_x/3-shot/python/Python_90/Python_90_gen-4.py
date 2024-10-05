    if len(lst) < 2:
        return None

    min_value = lst[0]
    min_index = 0
    for i, num in enumerate(lst):
        if num < min_value:
            min_value = num
            min_index = i

    if len(lst) == 2:
        return min_value

    if min_value == lst[-1]:
        return None

    return lst[min_index + 1]


