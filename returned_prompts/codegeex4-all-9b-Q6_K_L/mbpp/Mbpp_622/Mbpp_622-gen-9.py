def get_median(list1, list2, n):
    temp = sorted(list1 + list2)
    return (temp[n - 1] + temp[n]) / 2.0

