def div_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    result = []
    for i, j in zip(list1, list2):
        if j == 0:
            raise ValueError("Cannot divide by zero")
        result.append(i/j)
    return result