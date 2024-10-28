def multiply_elements(tup):
    return tuple(tup[i] * tup[i+1] for i in range(len(tup)-1))