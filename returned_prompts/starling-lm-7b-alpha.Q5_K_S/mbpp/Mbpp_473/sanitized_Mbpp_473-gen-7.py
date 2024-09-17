def tuple_intersection(*tuples):
    # Initialize an empty set to store the intersection of the tuples
    intersection = set()

    # Iterate over each tuple in the given tuples list
    for t in tuples:
        # Add all the elements of the tuple to the set
        intersection.update(t)

    return intersection