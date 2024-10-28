def division_elements(tup1, tup2):
    """
    This function takes in two tuples and performs mathematical division operation element-wise across the given tuples.
    """
    res = []
    for i in range(len(tup1)):
        res.append(tup1[i]/tup2[i])
    return tuple(res)