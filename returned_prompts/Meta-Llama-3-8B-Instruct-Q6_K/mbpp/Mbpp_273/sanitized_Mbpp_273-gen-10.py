def substract_elements(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(t1[i] - t2[i])
    return tuple(result)  # return the result as a tuple