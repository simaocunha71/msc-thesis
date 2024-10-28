    largest_neg = None
    smallest_pos = None

    for i in lst:
        if i < 0:
            if largest_neg == None or i > largest_neg:
                largest_neg = i
        elif i > 0:
            if smallest_pos == None or i < smallest_pos:
                smallest_pos = i

    return (largest_neg, smallest_pos)


