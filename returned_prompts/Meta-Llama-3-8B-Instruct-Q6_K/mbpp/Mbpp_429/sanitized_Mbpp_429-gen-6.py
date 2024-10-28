def and_tuples(tup1, tup2):
    result = []
    for i, j in zip(tup1, tup2):
        if i & j:
            result.append(1)
        else:
            result.append(0)
    return tuple(result)  # Convert list to tuple and return