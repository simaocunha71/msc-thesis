def index_minimum(tuples):
    return min(tuples, key=lambda x: x[1])[0]  # returns the first element of the tuple with the smallest second value.