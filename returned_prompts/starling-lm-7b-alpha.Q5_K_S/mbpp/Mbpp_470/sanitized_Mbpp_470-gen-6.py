def add_pairwise(tup):
    # Initialize result
    result = []
    # Traverse the given tuple
    for i in range(len(tup)-1):
        # Compute the sum of neighboring elements
        result.append(tup[i] + tup[i+1])
    # Append the last element of tuple
    result.append(tup[-1])
    return tuple(result)