def maximize_elements(tuple_list):
    """
    tuple_list: a list of tuples
    returns: a list of tuples
    """
    # Your code here
    return tuple(map(max, zip(*tuple_list)))