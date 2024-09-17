def get_median(list1, list2, n):
    result = []
    i = 0
    j = 0
    while i < n and j < n:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if i < n:
        result.extend(list1[i:])
    else:
        result.extend(list2[j:])

    if len(result) % 2 == 0:
        return (result[len(result) // 2 - 1] + result[len(result) // 2]) / 2.0
    else:
        return result[len(result) // 2]