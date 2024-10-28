    sorted_list = sorted(l)
    length = len(sorted_list)
    if length % 2 == 0:
        mid1 = length // 2
        mid2 = mid1 - 1
        median = (sorted_list[mid1] + sorted_list[mid2]) / 2.0
    else:
        median = sorted_list[length // 2]
    return median


