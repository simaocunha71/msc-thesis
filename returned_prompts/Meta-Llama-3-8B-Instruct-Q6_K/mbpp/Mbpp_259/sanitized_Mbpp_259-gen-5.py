def maximize_elements(t1, t2):
    max_elements = []
    for i in range(len(t1)):
        if t1[i][0] < t2[i][0]:
            max_elements.append(t2[i])
        else:
            max_elements.append(t1[i])
    return tuple(max_elements)  # convert list to tuple