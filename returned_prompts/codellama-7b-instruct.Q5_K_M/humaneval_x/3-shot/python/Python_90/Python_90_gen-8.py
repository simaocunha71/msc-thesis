    if len(lst) < 2:
        return None

    smallest = lst[0]
    second_smallest = None

    for i in range(1, len(lst)):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif second_smallest == None and lst[i] > smallest and lst[i] < second_smallest:
            second_smallest = lst[i]

    return second_smallest


