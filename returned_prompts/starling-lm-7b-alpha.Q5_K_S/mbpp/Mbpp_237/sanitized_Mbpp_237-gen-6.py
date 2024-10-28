def check_occurences(list_tuples):
    # Initialize a dictionary to store the number of occurrences for each tuple
    occurences = {}

    # Iterate through each tuple in the list
    for tuple_ in list_tuples:
        # Check if the tuple is already in the dictionary
        if tuple_ in occurences:
            # If it is, increment the count by 1
            occurences[tuple_] += 1
        # Otherwise, add the tuple to the dictionary and set the count to 1
        else:
            occurences[tuple_] = 1

    # Return the dictionary mapping each tuple to its number of occurrences
    return occurences