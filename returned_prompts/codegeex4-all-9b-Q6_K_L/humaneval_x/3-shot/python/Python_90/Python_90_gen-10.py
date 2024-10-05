    if len(lst) < 2:
        return None

    lst.sort()
    smallest = lst[0]
    second_smallest = None

    for num in lst:
        if num > smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num

    return second_smallest

