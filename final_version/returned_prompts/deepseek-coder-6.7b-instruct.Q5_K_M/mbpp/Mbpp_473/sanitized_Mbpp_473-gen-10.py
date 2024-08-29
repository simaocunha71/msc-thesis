def tuple_intersection(tuples):
    # Convert each tuple to a set
    sets = [set(t) for t in tuples]
    # Find the intersection of the first two sets
    intersection = sets[0].intersection(sets[1])
    # Find the intersection of the result with the next set, and so on
    for s in sets[2:]:
        intersection = intersection.intersection(s)
    # Return the intersection as a list of tuples
    return [t for t in intersection]