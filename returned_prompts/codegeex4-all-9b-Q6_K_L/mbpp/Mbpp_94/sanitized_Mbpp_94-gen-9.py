def index_minimum(tuples):
    # Find the index of the tuple with the smallest second value
    smallest_index = tuples.index(min(tuples, key=lambda x: x[1]))
    # Return the first value of that tuple
    return tuples[smallest_index][0]