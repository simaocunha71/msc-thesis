def check_occurences(tuples):
    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate over each tuple in the list
    for tup in tuples:
        # If the tuple is already in the dictionary, increment its count
        if tup in counts:
            counts[tup] += 1
        # If the tuple is not in the dictionary, add it with a count of 1
        else:
            counts[tup] = 1

    # Return the counts dictionary
    return counts