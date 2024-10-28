def maximize_elements(tuple1, tuple2):
    result = []
    for i in range(len(tuple1)):
        if tuple1[i][1] > tuple2[i][1]:
            result.append(tuple1[i])
        else:
            result.append(tuple2[i])
    return tuple(result)  # Convert the list to tuple and return