def get_median(list1, list2, size):
    total = 0
    for i in range(size):
        total += list1[i] + list2[i]
    return total / (2 * size)