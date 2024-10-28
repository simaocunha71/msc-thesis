def multiply_elements(tup):
    # Unpack the tuple
    t1, *t2 = tup

    # Multiply the elements
    result = []
    for i in range(len(t2)):
        result.append(t2[i] * t1)

    return tuple(result)


