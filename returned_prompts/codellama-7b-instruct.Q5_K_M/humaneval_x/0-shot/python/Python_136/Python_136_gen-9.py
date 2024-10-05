
def largest_smallest_integers(lst):
    largest_neg = None
    smallest_pos = None
    for i in lst:
        if i > 0 and smallest_pos == None:
            smallest_pos = i
        elif i > 0 and smallest_pos != None and i < smallest_pos:
            smallest_pos = i
        elif i < 0 and largest_neg == None:
            largest_neg = i
        elif i < 0 and largest_neg != None and i > largest_neg:
            largest_neg = i
    return (largest_neg, smallest_pos)