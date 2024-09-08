def index_minimum(tuples):
    # Sort the list of tuples by the second value in each tuple
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    # Return the first value of the first tuple in the sorted list
    return sorted_tuples[0][0]