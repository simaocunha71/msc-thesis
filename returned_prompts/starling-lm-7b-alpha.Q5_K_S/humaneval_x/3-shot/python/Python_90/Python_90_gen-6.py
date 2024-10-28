    smallest = None
    second_smallest = None
    for elem in lst:
        if smallest is None or elem < smallest:
            second_smallest = smallest
            smallest = elem
        elif second_smallest is None or elem < second_smallest:
            second_smallest = elem

    return second_smallest


