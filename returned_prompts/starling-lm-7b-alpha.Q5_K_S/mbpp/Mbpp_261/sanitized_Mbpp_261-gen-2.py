def division_elements(t1, t2):
    """
    Takes in two tuples and performs mathematical division operation element-wise across the given tuples.
    """
    result = []
    for i in range(len(t1)):
        result.append(t1[i]/t2[i])
    return tuple(result)