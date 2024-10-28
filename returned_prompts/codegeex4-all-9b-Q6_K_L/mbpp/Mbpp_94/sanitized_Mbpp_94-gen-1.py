def index_minimum(tuples):
    # find the tuple with minimum second value
    min_tuple = min(tuples, key=lambda x: x[1])
    
    # return the first value of the tuple with minimum second value
    return min_tuple[0]