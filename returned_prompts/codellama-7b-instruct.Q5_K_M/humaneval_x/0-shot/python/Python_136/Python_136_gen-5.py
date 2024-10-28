
def largest_smallest_integers(lst):
    largest = None
    smallest = None
    for i in lst:
        if i < 0 and (largest is None or i > largest):
            largest = i
        elif i > 0 and (smallest is None or i < smallest):
            smallest = i
    return (largest, smallest)