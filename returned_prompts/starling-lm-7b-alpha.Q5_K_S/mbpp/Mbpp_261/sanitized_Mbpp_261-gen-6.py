def division_elements(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return None
    else:
        result = []
        for i in range(len(tuple1)):
            result.append(tuple1[i]/tuple2[i])
        return tuple(result)