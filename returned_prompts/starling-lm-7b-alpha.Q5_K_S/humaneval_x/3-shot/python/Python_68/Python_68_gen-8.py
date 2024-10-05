    result = []
    for idx, elem in enumerate(arr):
        if elem % 2 == 0:
            if not result or elem < result[0][0]:
                result = [elem, idx]
            elif elem == result[0][0]:
                if idx < result[0][1]:
                    result[0] = [elem, idx]
    return result if result else []


