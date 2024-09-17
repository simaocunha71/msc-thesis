def division_elements(tup1, tup2):
    '''
    This function takes in two tuples and performs mathematical division operation element-wise across the given tuples.
    '''
    # Initialize result
    result = []
    # Iterate over tuples
    for i in range(len(tup1)):
        # Perform division
        result.append(tup1[i]/tup2[i])
    # Return result
    return result