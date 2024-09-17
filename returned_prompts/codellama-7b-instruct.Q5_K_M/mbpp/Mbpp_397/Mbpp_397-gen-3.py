
def median_numbers(a, b, c):
    median_list = sorted([a, b, c])
    length = len(median_list)
    if length % 2 == 0:
        return (median_list[length // 2 - 1] + median_list[length // 2]) / 2
    else:
        return median_list[length // 2]


