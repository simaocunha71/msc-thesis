def maximize_elements(tup1, tup2):
    result = []
    for i in range(len(tup1)):
        if tup1[i][0] < tup2[i][0]:
            result.append(tup2[i])
        elif tup1[i][0] > tup2[i][0]:
            result.append(tup1[i])
        else:
            if tup1[i][1] > tup2[i][1]:
                result.append(tup1[i])
            else:
                result.append(tup2[i])
    return result