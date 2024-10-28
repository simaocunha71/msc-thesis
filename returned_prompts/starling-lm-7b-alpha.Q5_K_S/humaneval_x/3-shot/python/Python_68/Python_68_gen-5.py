    result = [float("inf"), -1]
    for idx, elem in enumerate(arr):
        if elem % 2 == 0 and elem < result[0]:
            result[0] = elem
            result[1] = idx

    return result if result[0] != float("inf") else []


