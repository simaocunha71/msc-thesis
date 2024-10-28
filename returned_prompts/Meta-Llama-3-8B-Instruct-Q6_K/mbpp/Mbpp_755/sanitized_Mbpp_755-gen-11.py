def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst = sorted(set(lst))
    smallest = lst[0]
    count = 1
    for num in lst[1:]:
        if num == smallest:
            count += 1
        else:
            if count > 1:
                return smallest
            return num
    return None