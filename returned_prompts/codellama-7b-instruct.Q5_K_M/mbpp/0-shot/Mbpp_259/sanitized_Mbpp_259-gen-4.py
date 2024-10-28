def maximize_elements(tuple1, tuple2):
    max_tuple = []
    for i in range(len(tuple1)):
        for j in range(len(tuple2[i])):
            if tuple1[i][j] > tuple2[i][j]:
                max_tuple.append(tuple1[i])
                break
            else:
                max_tuple.append(tuple2[i])
    return max_tuple