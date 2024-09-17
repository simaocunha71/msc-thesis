def maximize_elements(tuple1, tuple2):
    # Create a list of tuples
    tuples = list(zip(tuple1, tuple2))
    # Sort the list of tuples based on the first element of tuple in descending order
    tuples.sort(key = lambda x: x[0], reverse = True)
    # Sort the list of tuples based on the second element of tuple in ascending order
    tuples.sort(key = lambda x: x[1])
    # Return the list of tuples
    return tuples